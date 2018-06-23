scriptencoding utf-8

" Copyright (c) 2017 Filip Szymański. All rights reserved.
" Use of this source code is governed by an MIT license that can be
" found in the LICENSE file.

" TODO: Better exception handling

function! s:templates_sink(templates) abort
  try
    let l:lines = _fzf_gitignore_create(a:templates)
  catch /^Vim(\(let\|return\)):/
    return
  endtry

  new
  setlocal filetype=gitignore

  call append(0, l:lines)

  $-1,$delete _
  normal! gg
endfunction

function! fzf_gitignore#run() abort
  try
    let l:opts = {
          \ 'source': _fzf_gitignore_supported_templates(),
          \ 'sink*': function('s:templates_sink'),
          \ 'options': '-m --prompt="Template> " --header="gitignore.io"'
          \ }
  catch /^Vim(\(let\|return\)):/
    return
  endtry

  call fzf#run(fzf#wrap(l:opts))
endfunction

" vim: ts=2 et sw=2
