#aliases
alias ls='ls -la --color=auto'

#config
autoload -U colors && colors
PROMPT="%~%{$fg[yellow]%}%#%{$reset_color%} " #prompt format
WORDCHARS='*?_-.[]~=&;!#$%^(){}<>' #word non-delimiter

#history
HISTSIZE=1000
SAVEHIST=1000
HISTFILE=~/.zsh_history
setopt INC_APPEND_HISTORY SHARE_HISTORY HIST_SAVE_NO_DUPS

#history incremental preserving pattern search backward
autoload -Uz narrow-to-region
function _history-incremental-preserving-pattern-search-backward
{
    local state
    MARK=CURSOR  # magick, else multiple ^R don't work
    narrow-to-region -p "$LBUFFER${BUFFER:+>}" -P "${BUFFER:+<}$RBUFFER" -S state
    zle end-of-history
    zle history-incremental-pattern-search-backward
    narrow-to-region -R state
}
zle -N _history-incremental-preserving-pattern-search-backward
bindkey "^R" _history-incremental-preserving-pattern-search-backward
bindkey -M isearch "^R" history-incremental-pattern-search-backward
bindkey "^S" history-incremental-pattern-search-forward

#jobs
setopt NO_HUP NO_CHECK_JOBS #no HUP signal to bg jobs upon shell exit


