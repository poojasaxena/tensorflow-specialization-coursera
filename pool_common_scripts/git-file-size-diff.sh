#!/bin/bash
USAGE='[--cached] [<rev-list-options>...]

Show file size changes between two commits or the index and a commit.'

. "$(git --exec-path)/git-sh-setup"
args=$(git rev-parse --sq "$@")
[ -n "$args" ] || usage
cmd="diff-tree -r"
[[ $args =~ "--cached" ]] && cmd="diff-index"
eval "git $cmd $args" | {
  total=0
  while read A B C D M P
  do
    case $M in
      M) bytes=$(( $(git cat-file -s $D) - $(git cat-file -s $C) )) ;;
      A) bytes=$(git cat-file -s $D) ;;
      D) bytes=-$(git cat-file -s $C) ;;
      *)
        echo >&2 warning: unhandled mode $M in \"$A $B $C $D $M $P\"
        continue
        ;;
    esac
    total=$(( $total + $bytes ))
    printf '%d\t%s\n' $bytes "$P"
  done
  echo total $total
}

# reference: https://stackoverflow.com/questions/10845051/git-show-total-file-size-difference-between-two-commits/10847242#10847242
# usage: git file-size-diff <tree-ish> <tree-ish>
# usage: git file-size-diff HEAD~850..HEAD~845
# HEAD~850 is 850 commits before HEAD. It is just another notation for a commit and yes you can use a specific commit id or a tag or anything that can be resolved to a commit. The script uses git rev-parse so see the manual section "Specifying Revisions" in the git-rev-parse documentation for the full details. (git-scm.com/docs/git-rev-parse)
# git-rev-parse
