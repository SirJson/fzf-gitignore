scriptencoding utf-8

" Copyright (c) 2017 Filip Szymański. All rights reserved.
" Use of this source code is governed by an MIT license that can be
" found in the LICENSE file.

if exists('b:current_syntax')
  finish
endif

syntax keyword gitignoreTodo TODO FIXME XXX NOTE SEE contained
syntax match gitignoreComment '^#.*' contains=gitignoreTodo
syntax match gitignoreComment '\s#.*'ms=s+1 contains=gitignoreTodo

highlight default link gitignoreTodo Todo
highlight default link gitignoreComment Comment

let b:current_syntax = 'gitignore'

" vim: ts=2 et sw=2
