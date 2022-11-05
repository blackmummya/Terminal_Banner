from socket import gethostname
from os import getgid, system
from json import dump, load
from platform import node
from sys import exit, stdout
from time import sleep


class C:
    BLUE = '\033[1;34m'
    GREEN = '\033[1;32m'
    RED = '\033[1;31m'
    WHITE = '\033[1;37m'
    CYAN = '\033[1;36m'
    YELLOW = '\033[1;33m'
    CRIMSON = '\033[1;38m'
    RESET = '\033[0m'
    IND = '\033[04m'
    LIGHTRED = '\033[91m'
    MAGANTA = '\033[95m'
    ANIMATION = '\033[05m'


def sudo_check(root):
    if getgid() == root:
        pass
    else:
        exit(C.RED + '[' + C.YELLOW + C.ANIMATION + '!' + C.RESET + C.RED + ']' + ' Run it as root!'.title())


def get_stored_req():
    file_name = '/usr/bin/user.json'
    try:
        with open(file_name) as f:
            user_node = load(f)
    except FileNotFoundError:
        return None
    else:
        return user_node


def get_new_req():
    user_node = get_stored_req()
    if user_node:
        pass
    else:
        user_node = node()
        file_name = '/usr/bin/user.json'
        with open(file_name, 'w') as f:
            dump(user_node, f)
            lst_n = ['10', '20', '30', '40', '50', '60', '70', '80', '90', '100']
            lst_l = ['===', '======', '=========', '============', '===============', '=================='
                     , '=====================', '========================',
                     '===========================', '==============================']
            system('apt-get install git; clear')
            system('apt-get install lolcat; clear')
            system('apt-get install figlet lolcat; clear')
            print(C.YELLOW + '[' + C.GREEN + C.ANIMATION + '*' + C.RESET + C.RED + ']' + C.CYAN + ' please wait...'.title())
            for i, l in zip(lst_n, lst_l):
                sleep(1)
                print(C.RESET + f'\r{l} {i}%', end=''), stdout.flush()
            print(C.RESET + C.GREEN + 'Done.')


text_banner = input(C.YELLOW + '[' + C.ANIMATION + '💀' + C.RESET + C.RED + ']'
                    + C.CYAN + C.MAGANTA + ' enter your text: '.title())


def style():
    system('clear')
    print(C.YELLOW + '[' + C.GREEN + '1' + C.RED + ']' + C.CYAN + ' Elite Font.\n')
    system(f'figlet -f Elite "{text_banner.upper()}" | lolcat')

    print('\n' + C.YELLOW + '[' + C.GREEN + '2' + C.RED + ']' + C.CYAN + ' 1Row Font.\n')
    system(f'figlet -f 1Row "{text_banner.upper()}" | lolcat')

    print('\n' + C.YELLOW + '[' + C.GREEN + '3' + C.RED + ']' + C.CYAN + ' 3D-ASCII Font.\n')
    system(f'figlet -f 3D-ASCII "{text_banner.upper()}" | lolcat')

    print('\n' + C.YELLOW + '[' + C.GREEN + '4' + C.RED + ']' + C.CYAN + ' 3d Font.\n')
    system(f'figlet -f 3d "{text_banner.upper()}" | lolcat')

    print('\n' + C.YELLOW + '[' + C.GREEN + '5' + C.RED + ']' + C.CYAN + ' 4Max Font.\n')
    system(f'figlet -f 4Max "{text_banner.upper()}" | lolcat')

    print('\n' + C.YELLOW + '[' + C.GREEN + '6' + C.RED + ']' + C.CYAN + ' Alphabet Font.\n')
    system(f'figlet -f Alphabet "{text_banner.upper()}" | lolcat')

    print('\n' + C.YELLOW + '[' + C.GREEN + '7' + C.RED + ']' + C.CYAN + ' amc3line Font.\n')
    system(f'figlet -f amc3line "{text_banner.upper()}" | lolcat')

    print('\n' + C.YELLOW + '[' + C.GREEN + '8' + C.RED + ']' + C.CYAN + ' amcaaa01 Font.\n')
    system(f'figlet -f amcaaa01 "{text_banner.upper()}" | lolcat')

    print('\n' + C.YELLOW + '[' + C.GREEN + '9' + C.RED + ']' + C.CYAN + ' amcrazo2 Font.\n')
    system(f'figlet -f amcrazo2 "{text_banner.upper()}" | lolcat')

    print('\n' + C.YELLOW + '[' + C.GREEN + '10' + C.RED + ']' + C.CYAN + ' amcslder Font.\n')
    system(f'figlet -f amcslder "{text_banner.upper()}" | lolcat')

    print('\n' + C.YELLOW + '[' + C.GREEN + '11' + C.RED + ']' + C.CYAN + ' amcthin Font.\n')
    system(f'figlet -f amcthin "{text_banner.upper()}" | lolcat')

    print('\n' + C.YELLOW + '[' + C.GREEN + '12' + C.RED + ']' + C.CYAN + ' Thin Font.\n')
    system(f'figlet -f Thin "{text_banner.upper()}" | lolcat')

    print('\n' + C.YELLOW + '[' + C.GREEN + '13' + C.RED + ']' + C.CYAN + ' Shadow Font.\n')
    system(f'figlet -f Shadow "{text_banner.upper()}" | lolcat')

    print('\n' + C.YELLOW + '[' + C.GREEN + '14' + C.RED + ']' + C.CYAN + ' Arrows Font.\n')
    system(f'figlet -f Arrows "{text_banner.upper()}" | lolcat')

    print('\n' + C.YELLOW + '[' + C.GREEN + '15' + C.RED + ']' + C.CYAN + ' Avatar Font.\n')
    system(f'figlet -f Avatar "{text_banner.upper()}" | lolcat')

    print('\n' + C.YELLOW + '[' + C.GREEN + '16' + C.RED + ']' + C.CYAN + ' Bell Font.\n')
    system(f'figlet -f Bell "{text_banner.upper()}" | lolcat')

    print('\n' + C.YELLOW + '[' + C.GREEN + '17' + C.RED + ']' + C.CYAN + ' Big Font.\n')
    system(f'figlet -f Big "{text_banner.upper()}" | lolcat')

    print('\n' + C.YELLOW + '[' + C.GREEN + '18' + C.RED + ']' + C.CYAN + ' Block Font.\n')
    system(f'figlet -f Block "{text_banner.upper()}" | lolcat')

    print('\n' + C.YELLOW + '[' + C.GREEN + '19' + C.RED + ']' + C.CYAN + ' Bloody Font.\n')
    system(f'figlet -f Bloody "{text_banner.upper()}" | lolcat')

    print('\n' + C.YELLOW + '[' + C.GREEN + '20' + C.RED + ']' + C.CYAN + ' Crawford2 Font.\n')
    system(f'figlet -f Crawford2 "{text_banner.upper()}" | lolcat')

    print('\n' + C.YELLOW + '[' + C.GREEN + '21' + C.RED + ']' + C.CYAN + ' Cursive Font.\n')
    system(f'figlet -f Cursive "{text_banner.upper()}" | lolcat')

    print('\n' + C.YELLOW + '[' + C.GREEN + '22' + C.RED + ']' + C.CYAN + ' Cybermedium Font.\n')
    system(f'figlet -f Cybermedium "{text_banner.upper()}" | lolcat')

    print('\n' + C.YELLOW + '[' + C.GREEN + '23' + C.RED + ']' + C.CYAN + ' dietcola Font.\n')
    system(f'figlet -f dietcola "{text_banner.upper()}" | lolcat')

    print('\n' + C.YELLOW + '[' + C.GREEN + '24' + C.RED + ']' + C.CYAN + ' Doom Font.\n')
    system(f'figlet -f Doom "{text_banner.upper()}" | lolcat')

    print('\n' + C.YELLOW + '[' + C.GREEN + '25' + C.RED + ']' + C.CYAN + ' Electronic Font.\n')
    system(f'figlet -f Electronic "{text_banner.upper()}" | lolcat')


path = f'/home/{gethostname().lower()}/.zshrc'


def re_conf():
    configuration_file = """# ~/.zshrc file for zsh interactive shells.
    # see /usr/share/doc/zsh/examples/zshrc for examples

    setopt autocd              # change directory just by typing its name
    #setopt correct            # auto correct mistakes
    setopt interactivecomments # allow comments in interactive mode
    setopt magicequalsubst     # enable filename expansion for arguments of the form ‘anything=expression’
    setopt nonomatch           # hide error message if there is no match for the pattern
    setopt notify              # report the status of background jobs immediately
    setopt numericglobsort     # sort filenames numerically when it makes sense
    setopt promptsubst         # enable command substitution in prompt

    WORDCHARS=${WORDCHARS//\/} # Don't consider certain characters part of the word

    # hide EOL sign ('%')
    PROMPT_EOL_MARK=""

    # configure key keybindings
    bindkey -e                                        # emacs key bindings
    bindkey ' ' magic-space                           # do history expansion on space
    bindkey '^U' backward-kill-line                   # ctrl + U
    bindkey '^[[3;5~' kill-word                       # ctrl + Supr
    bindkey '^[[3~' delete-char                       # delete
    bindkey '^[[1;5C' forward-word                    # ctrl + ->
    bindkey '^[[1;5D' backward-word                   # ctrl + <-
    bindkey '^[[5~' beginning-of-buffer-or-history    # page up
    bindkey '^[[6~' end-of-buffer-or-history          # page down
    bindkey '^[[H' beginning-of-line                  # home
    bindkey '^[[F' end-of-line                        # end
    bindkey '^[[Z' undo                               # shift + tab undo last action

    # enable completion features
    autoload -Uz compinit
    compinit -d ~/.cache/zcompdump
    zstyle ':completion:*:*:*:*:*' menu select
    zstyle ':completion:*' auto-description 'specify: %d'
    zstyle ':completion:*' completer _expand _complete
    zstyle ':completion:*' format 'Completing %d'
    zstyle ':completion:*' group-name ''
    zstyle ':completion:*' list-colors ''
    zstyle ':completion:*' list-prompt %SAt %p: Hit TAB for more, or the character to insert%s
    zstyle ':completion:*' matcher-list 'm:{a-zA-Z}={A-Za-z}'
    zstyle ':completion:*' rehash true
    zstyle ':completion:*' select-prompt %SScrolling active: current selection at %p%s
    zstyle ':completion:*' use-compctl false
    zstyle ':completion:*' verbose true
    zstyle ':completion:*:kill:*' command 'ps -u $USER -o pid,%cpu,tty,cputime,cmd'

    # History configurations
    HISTFILE=~/.zsh_history
    HISTSIZE=1000
    SAVEHIST=2000
    setopt hist_expire_dups_first # delete duplicates first when HISTFILE size exceeds HISTSIZE
    setopt hist_ignore_dups       # ignore duplicated commands history list
    setopt hist_ignore_space      # ignore commands that start with space
    setopt hist_verify            # show command with history expansion to user before running it
    #setopt share_history         # share command history data

    # force zsh to show the complete history
    alias history="history 0"

    # configure `time` format
    TIMEFMT=$'\\nreal\\t%E\\nuser\\t%U\\nsys\\t%S\\ncpu\\t%P'

    # make less more friendly for non-text input files, see lesspipe(1)
    #[ -x /usr/bin/lesspipe ] && eval "$(SHELL=/bin/sh lesspipe)"

    # set variable identifying the chroot you work in (used in the prompt below)
    if [ -z "${debian_chroot:-}" ] && [ -r /etc/debian_chroot ]; then
        debian_chroot=$(cat /etc/debian_chroot)
    fi

    # set a fancy prompt (non-color, unless we know we "want" color)
    case "$TERM" in
        xterm-color|*-256color) color_prompt=yes;;
    esac

    # uncomment for a colored prompt, if the terminal has the capability; turned
    # off by default to not distract the user: the focus in a terminal window
    # should be on the output of commands, not on the prompt
    force_color_prompt=yes

    if [ -n "$force_color_prompt" ]; then
        if [ -x /usr/bin/tput ] && tput setaf 1 >&/dev/null; then
            # We have color support; assume it's compliant with Ecma-48
            # (ISO/IEC-6429). (Lack of such support is extremely rare, and such
            # a case would tend to support setf rather than setaf.)
            color_prompt=yes
        else
            color_prompt=
        fi
    fi

    configure_prompt() {
        prompt_symbol=㉿
        # Skull emoji for root terminal
        #[ "$EUID" -eq 0 ] && prompt_symbol=💀
        case "$PROMPT_ALTERNATIVE" in
            twoline)
                PROMPT=$'%F{%(#.blue.green)}┌──${debian_chroot:+($debian_chroot)─}${VIRTUAL_ENV:+($(basename $VIRTUAL_ENV))─}(%B%F{%(#.red.blue)}%n'$prompt_symbol$'%m%b%F{%(#.blue.green)})-[%B%F{reset}%(6~.%-1~/…/%4~.%5~)%b%F{%(#.blue.green)}]\n└─%B%(#.%F{red}#.%F{blue}$)%b%F{reset} '
                # Right-side prompt with exit codes and background processes
                #RPROMPT=$'%(?.. %? %F{red}%B⨯%b%F{reset})%(1j. %j %F{yellow}%B⚙%b%F{reset}.)'
                ;;
            oneline)
                PROMPT=$'${debian_chroot:+($debian_chroot)}${VIRTUAL_ENV:+($(basename $VIRTUAL_ENV))}%B%F{%(#.red.blue)}%n@%m%b%F{reset}:%B%F{%(#.blue.green)}%~%b%F{reset}%(#.#.$) '
                RPROMPT=
                ;;
            backtrack)
                PROMPT=$'${debian_chroot:+($debian_chroot)}${VIRTUAL_ENV:+($(basename $VIRTUAL_ENV))}%B%F{red}%n@%m%b%F{reset}:%B%F{blue}%~%b%F{reset}%(#.#.$) '
                RPROMPT=
                ;;
        esac
        unset prompt_symbol
    }

    # The following block is surrounded by two delimiters.
    # These delimiters must not be modified. Thanks.
    # START KALI CONFIG VARIABLES
    PROMPT_ALTERNATIVE=twoline
    NEWLINE_BEFORE_PROMPT=yes
    # STOP KALI CONFIG VARIABLES

    if [ "$color_prompt" = yes ]; then
        # override default virtualenv indicator in prompt
        VIRTUAL_ENV_DISABLE_PROMPT=1

        configure_prompt

        # enable syntax-highlighting
        if [ -f /usr/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh ]; then
            . /usr/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
            ZSH_HIGHLIGHT_HIGHLIGHTERS=(main brackets pattern)
            ZSH_HIGHLIGHT_STYLES[default]=none
            ZSH_HIGHLIGHT_STYLES[unknown-token]=fg=white,underline
            ZSH_HIGHLIGHT_STYLES[reserved-word]=fg=cyan,bold
            ZSH_HIGHLIGHT_STYLES[suffix-alias]=fg=green,underline
            ZSH_HIGHLIGHT_STYLES[global-alias]=fg=green,bold
            ZSH_HIGHLIGHT_STYLES[precommand]=fg=green,underline
            ZSH_HIGHLIGHT_STYLES[commandseparator]=fg=blue,bold
            ZSH_HIGHLIGHT_STYLES[autodirectory]=fg=green,underline
            ZSH_HIGHLIGHT_STYLES[path]=bold
            ZSH_HIGHLIGHT_STYLES[path_pathseparator]=
            ZSH_HIGHLIGHT_STYLES[path_prefix_pathseparator]=
            ZSH_HIGHLIGHT_STYLES[globbing]=fg=blue,bold
            ZSH_HIGHLIGHT_STYLES[history-expansion]=fg=blue,bold
            ZSH_HIGHLIGHT_STYLES[command-substitution]=none
            ZSH_HIGHLIGHT_STYLES[command-substitution-delimiter]=fg=magenta,bold
            ZSH_HIGHLIGHT_STYLES[process-substitution]=none
            ZSH_HIGHLIGHT_STYLES[process-substitution-delimiter]=fg=magenta,bold
            ZSH_HIGHLIGHT_STYLES[single-hyphen-option]=fg=green
            ZSH_HIGHLIGHT_STYLES[double-hyphen-option]=fg=green
            ZSH_HIGHLIGHT_STYLES[back-quoted-argument]=none
            ZSH_HIGHLIGHT_STYLES[back-quoted-argument-delimiter]=fg=blue,bold
            ZSH_HIGHLIGHT_STYLES[single-quoted-argument]=fg=yellow
            ZSH_HIGHLIGHT_STYLES[double-quoted-argument]=fg=yellow
            ZSH_HIGHLIGHT_STYLES[dollar-quoted-argument]=fg=yellow
            ZSH_HIGHLIGHT_STYLES[rc-quote]=fg=magenta
            ZSH_HIGHLIGHT_STYLES[dollar-double-quoted-argument]=fg=magenta,bold
            ZSH_HIGHLIGHT_STYLES[back-double-quoted-argument]=fg=magenta,bold
            ZSH_HIGHLIGHT_STYLES[back-dollar-quoted-argument]=fg=magenta,bold
            ZSH_HIGHLIGHT_STYLES[assign]=none
            ZSH_HIGHLIGHT_STYLES[redirection]=fg=blue,bold
            ZSH_HIGHLIGHT_STYLES[comment]=fg=black,bold
            ZSH_HIGHLIGHT_STYLES[named-fd]=none
            ZSH_HIGHLIGHT_STYLES[numeric-fd]=none
            ZSH_HIGHLIGHT_STYLES[arg0]=fg=cyan
            ZSH_HIGHLIGHT_STYLES[bracket-error]=fg=red,bold
            ZSH_HIGHLIGHT_STYLES[bracket-level-1]=fg=blue,bold
            ZSH_HIGHLIGHT_STYLES[bracket-level-2]=fg=green,bold
            ZSH_HIGHLIGHT_STYLES[bracket-level-3]=fg=magenta,bold
            ZSH_HIGHLIGHT_STYLES[bracket-level-4]=fg=yellow,bold
            ZSH_HIGHLIGHT_STYLES[bracket-level-5]=fg=cyan,bold
            ZSH_HIGHLIGHT_STYLES[cursor-matchingbracket]=standout
        fi
    else
        PROMPT='${debian_chroot:+($debian_chroot)}%n@%m:%~%(#.#.$) '
    fi
    unset color_prompt force_color_prompt

    toggle_oneline_prompt(){
        if [ "$PROMPT_ALTERNATIVE" = oneline ]; then
            PROMPT_ALTERNATIVE=twoline
        else
            PROMPT_ALTERNATIVE=oneline
        fi
        configure_prompt
        zle reset-prompt
    }
    zle -N toggle_oneline_prompt
    bindkey ^P toggle_oneline_prompt

    # If this is an xterm set the title to user@host:dir
    case "$TERM" in
    xterm*|rxvt*|Eterm|aterm|kterm|gnome*|alacritty)
        TERM_TITLE=$'\e]0;${debian_chroot:+($debian_chroot)}${VIRTUAL_ENV:+($(basename $VIRTUAL_ENV))}%n@%m: %~\a'
        ;;
    *)
        ;;
    esac

    precmd() {
        # Print the previously configured title
        print -Pnr -- "$TERM_TITLE"

        # Print a new line before the prompt, but only if it is not the first line
        if [ "$NEWLINE_BEFORE_PROMPT" = yes ]; then
            if [ -z "$_NEW_LINE_BEFORE_PROMPT" ]; then
                _NEW_LINE_BEFORE_PROMPT=1
            else
                print ""
            fi
        fi
    }

    # enable color support of ls, less and man, and also add handy aliases
    if [ -x /usr/bin/dircolors ]; then
        test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"
        export LS_COLORS="$LS_COLORS:ow=30;44:" # fix ls color for folders with 777 permissions

        alias ls='ls --color=auto'
        #alias dir='dir --color=auto'
        #alias vdir='vdir --color=auto'

        alias grep='grep --color=auto'
        alias fgrep='fgrep --color=auto'
        alias egrep='egrep --color=auto'
        alias diff='diff --color=auto'
        alias ip='ip --color=auto'

        export LESS_TERMCAP_mb=$'\E[1;31m'     # begin blink
        export LESS_TERMCAP_md=$'\E[1;36m'     # begin bold
        export LESS_TERMCAP_me=$'\E[0m'        # reset bold/blink
        export LESS_TERMCAP_so=$'\E[01;33m'    # begin reverse video
        export LESS_TERMCAP_se=$'\E[0m'        # reset reverse video
        export LESS_TERMCAP_us=$'\E[1;32m'     # begin underline
        export LESS_TERMCAP_ue=$'\E[0m'        # reset underline

        # Take advantage of $LS_COLORS for completion as well
        zstyle ':completion:*' list-colors "${(s.:.)LS_COLORS}"
        zstyle ':completion:*:*:kill:*:processes' list-colors '=(#b) #([0-9]#)*=0=01;31'
    fi

    # some more ls aliases
    alias ll='ls -l'
    alias la='ls -A'
    alias l='ls -CF'

    # enable auto-suggestions based on the history
    if [ -f /usr/share/zsh-autosuggestions/zsh-autosuggestions.zsh ]; then
        . /usr/share/zsh-autosuggestions/zsh-autosuggestions.zsh
        # change suggestion color
        ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE='fg=#999'
    fi

    # enable command-not-found if installed
    if [ -f /etc/zsh_command_not_found ]; then
        . /etc/zsh_command_not_found
    fi
    """
    with open(path, 'w') as zhell:
        zhell.write(configuration_file)


def applying():
    choose = int(input('\n\n' + C.YELLOW + '[' + C.GREEN + C.ANIMATION + '*'
                       + C.RESET + C.RED + ']' + C.CYAN + ' Choose: '))

    if choose == 1:
        re_conf()
        with open(path, 'a') as f:
            f.write(f'\nfiglet -f Elite "{text_banner.upper()}" | lolcat')
    elif choose == 2:
        re_conf()
        with open(path, 'a') as f:
            f.write(f'\nfiglet -f 1Row "{text_banner.upper()}" | lolcat')
    elif choose == 3:
        re_conf()
        with open(path, 'a') as f:
            f.write(f'\nfiglet -f 3D-ASCII "{text_banner.upper()}" | lolcat')
    elif choose == 4:
        re_conf()
        with open(path, 'a') as f:
            f.write(f'\nfiglet -f 3d "{text_banner.upper()}" | lolcat')
    elif choose == 5:
        re_conf()
        with open(path, 'a') as f:
            f.write(f'\nfiglet -f 4Max "{text_banner.upper()}" | lolcat')
    elif choose == 6:
        re_conf()
        with open(path, 'a') as f:
            f.write(f'\nfiglet -f Alphabet "{text_banner.upper()}" | lolcat')
    elif choose == 7:
        re_conf()
        with open(path, 'a') as f:
            f.write(f'\nfiglet -f amc3line "{text_banner.upper()}" | lolcat')
    elif choose == 8:
        re_conf()
        with open(path, 'a') as f:
            f.write(f'\nfiglet -f amcaaa01 "{text_banner.upper()}" | lolcat')
    elif choose == 9:
        re_conf()
        with open(path, 'a') as f:
            f.write(f'\nfiglet -f amcrazo2 "{text_banner.upper()}" | lolcat')
    elif choose == 10:
        re_conf()
        with open(path, 'a') as f:
            f.write(f'\nfiglet -f amcslder "{text_banner.upper()}" | lolcat')
    elif choose == 11:
        re_conf()
        with open(path, 'a') as f:
            f.write(f'\nfiglet -f amcthin "{text_banner.upper()}" | lolcat')
    elif choose == 12:
        re_conf()
        with open(path, 'a') as f:
            f.write(f'\nfiglet -f Thin "{text_banner.upper()}" | lolcat')
    elif choose == 13:
        re_conf()
        with open(path, 'a') as f:
            f.write(f'\nfiglet -f Shadow "{text_banner.upper()}" | lolcat')
    elif choose == 14:
        re_conf()
        with open(path, 'a') as f:
            f.write(f'\nfiglet -f Arrows "{text_banner.upper()}" | lolcat')
    elif choose == 15:
        re_conf()
        with open(path, 'a') as f:
            f.write(f'\nfiglet -f Avatar "{text_banner.upper()}" | lolcat')
    elif choose == 16:
        re_conf()
        with open(path, 'a') as f:
            f.write(f'\nfiglet -f Bell "{text_banner.upper()}" | lolcat')
    elif choose == 17:
        re_conf()
        with open(path, 'a') as f:
            f.write(f'\nfiglet -f Big "{text_banner.upper()}" | lolcat')
    elif choose == 18:
        re_conf()
        with open(path, 'a') as f:
            f.write(f'\nfiglet -f Block "{text_banner.upper()}" | lolcat')
    elif choose == 19:
        re_conf()
        with open(path, 'a') as f:
            f.write(f'\nfiglet -f Bloody "{text_banner.upper()}" | lolcat')
    elif choose == 20:
        re_conf()
        with open(path, 'a') as f:
            f.write(f'\nfiglet -f Crawford2 "{text_banner.upper()}" | lolcat')
    elif choose == 21:
        re_conf()
        with open(path, 'a') as f:
            f.write(f'\nfiglet -f Cursive "{text_banner.upper()}" | lolcat')
    elif choose == 22:
        re_conf()
        with open(path, 'a') as f:
            f.write(f'\nfiglet -f Cybermedium "{text_banner.upper()}" | lolcat')
    elif choose == 23:
        re_conf()
        with open(path, 'a') as f:
            f.write(f'\nfiglet -f dietcola "{text_banner.upper()}" | lolcat')
    elif choose == 24:
        re_conf()
        with open(path, 'a') as f:
            f.write(f'\nfiglet -f Doom "{text_banner.upper()}" | lolcat')
    elif choose == 25:
        re_conf()
        with open(path, 'a') as f:
            f.write(f'\nfiglet -f Electronic "{text_banner.upper()}" | lolcat')


if __name__ == '__main__':
    try:
        sudo_check(0)
        get_new_req()
        style()
        applying()
    except KeyboardInterrupt:
        print('bye')
    except Exception as Err:
        print(C.RED + '[' + C.YELLOW + C.ANIMATION + '!' + C.RESET + C.RED + ']' + f'{Err}')
