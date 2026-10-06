const fs=require('node:fs'),vm=require('node:vm'),assert=require('node:assert/strict');
const html=fs.readFileSync(require('node:path').join(__dirname,'../index.html'),'utf8');
const code=html.slice(html.indexOf('  const syncProjectIndex ='),html.indexOf('  let activePanel = null;'));
assert.ok(code.includes('syncProjectIndex();'));
let cards=[],panels={};const count={textContent:''};
function add(id){const position={textContent:''};panels[id]={querySelector:()=>position,position};const category={dataset:{projectCategory:'Research'},textContent:''};cards.push({id,category,querySelector:q=>q==='[data-dialog]'?{dataset:{dialog:id}}:category});}
for(let i=0;i<8;i++)add('p'+i);
const document={querySelectorAll:q=>{assert.equal(q,'.work-grid .work-card');return cards;},querySelector:q=>{assert.equal(q,'[data-project-count]');return count;},getElementById:id=>panels[id]};
const ctx=vm.createContext({document});vm.runInContext(code,ctx);
assert.equal(count.textContent,'08 projects');assert.equal(panels.p0.position.textContent,'Project notes / 01 of 08');assert.equal(panels.p7.position.textContent,'Project notes / 08 of 08');
add('p8');vm.runInContext('syncProjectIndex()',ctx);assert.equal(panels.p8.position.textContent,'Project notes / 09 of 09');assert.equal(count.textContent,'09 projects');
cards.unshift(cards.pop());vm.runInContext('syncProjectIndex()',ctx);assert.equal(panels.p8.position.textContent,'Project notes / 01 of 09');assert.equal(panels.p0.position.textContent,'Project notes / 02 of 09');assert.equal(cards[0].category.textContent,'01 / Research');
cards=cards.filter(c=>c.id!=='p3');vm.runInContext('syncProjectIndex()',ctx);assert.equal(count.textContent,'08 projects');assert.equal(panels.p7.position.textContent,'Project notes / 08 of 08');
cards.push(cards[0]);vm.runInContext('syncProjectIndex()',ctx);assert.equal(count.textContent,'08 projects');
cards=[cards[0]];vm.runInContext('syncProjectIndex()',ctx);assert.equal(count.textContent,'01 project');
cards=[];vm.runInContext('syncProjectIndex()',ctx);assert.equal(count.textContent,'00 projects');
console.log('PASS: initial 8, add 9th, reorder, remove, deduplicate, single and empty.');
