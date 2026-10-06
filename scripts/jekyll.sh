#!/bin/sh
# Use the isolated local toolchain; never install or update dependencies here.
set -eu
cd "$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)"
if [ -n "${PORTFOLIO_RUBY_BIN:-}" ]; then
  PATH="$PORTFOLIO_RUBY_BIN:$PATH"
elif [ -d /opt/homebrew/opt/ruby@3.3/bin ]; then
  PATH="/opt/homebrew/opt/ruby@3.3/bin:$PATH"
elif [ -d /usr/local/opt/ruby@3.3/bin ]; then
  PATH="/usr/local/opt/ruby@3.3/bin:$PATH"
fi
export PATH
BUILD_HOME="${PORTFOLIO_BUILD_HOME:-$HOME/.local/share/portfolio-build}"
export GEM_HOME="$BUILD_HOME/tooling"
export GEM_PATH="$GEM_HOME"
export BUNDLE_PATH="$BUILD_HOME/bundle"
export BUNDLE_FROZEN=true
if [ ! -x "$GEM_HOME/bin/bundle" ]; then
  echo 'Isolated Bundler is missing. Follow the build setup in README.md.' >&2
  exit 1
fi
if [ "$#" -eq 0 ]; then set -- build; fi
exec "$GEM_HOME/bin/bundle" _2.4.22_ exec jekyll "$@"
