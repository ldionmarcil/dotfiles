#aliases
alias ls='ls -la --color=auto'
alias grep='grep --color'
alias gdb='gdb -q'

#imports
autoload -U colors && colors
autoload -U compinit && compinit

#config
PROMPT="[%{$fg[$NCOLOR]%}%B%n%b%{$reset_color%}:%{$fg[red]%}%30<...<%~%<<%{$reset_color%}]%(!.#.$) "
WORDCHARS='*?_-[]~=&;!#$%^(){}<>' #word non-delimiter

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

#make user color in prompt different for root and users
if [ $UID -eq 0 ]; then NCOLOR="green"; else NCOLOR="white"; fi

if [[ "$TERM" == "dumb" ]]
then
    unsetopt zle
    unsetopt prompt_cr
    unsetopt prompt_subst
    PS1='$ '
fi

#removes orphan packages
orphans() {
  if [[ ! -n $(pacman -Qdt) ]]; then
    echo "No orphans to remove."
  else
    sudo pacman -Rns $(pacman -Qdtq)
  fi
}
