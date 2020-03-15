# Copyright (c) 2017-2020 Filip Szymański. All rights reserved.
# Use of this source code is governed by an MIT license that can be
# found in the LICENSE file.

import re
import socket
import urllib.error
import urllib.request

import pynvim

__version__ = '1.1'

API_URL = 'https://www.gitignore.io/api/{}'
USER_AGENT = 'fzf-gitignore/{} (https://github.com/fszymanski/fzf-gitignore)'.format(__version__)


@pynvim.plugin
class FzfGitignore():
    def __init__(self, nvim):
        self.__cache = None
        self.__nvim = nvim
        self.__pattern = re.compile(r'\n')

    def __error(self, msg):
        self.__nvim.command(
            'echohl ErrorMsg | echomsg "[fzf-gitignore] {}" | echohl None'.format(msg))

    def __fetch(self, params):
        req = urllib.request.Request(API_URL.format(params))
        req.add_header('User-Agent', USER_AGENT)
        try:
            with urllib.request.urlopen(req, timeout=30) as f:
                data = f.read().decode('utf-8')

                if 'Content-Length' in f.info():
                    if len(data) != int(f.info()['Content-Length']):
                        raise urllib.error.URLError('Download incomplete')

                return data
        except (urllib.error.HTTPError, urllib.error.URLError) as err:
            self.__error('{}: {}'.format(err, req.get_full_url()))
            raise
        except socket.error as err:
            self.__error('Socket error: {}: {}'.format(err, req.get_full_url()))
            raise
        except socket.timeout as err:
            self.__error('Connection timed out: {}: {}'.format(err, req.get_full_url()))
            raise

    @pynvim.function('_fzf_gitignore_supported_templates', sync=True)
    def supported_templates(self, args):
        if self.__cache is None:
            data = self.__pattern.sub(',', self.__fetch('list'))
            self.__cache = data.split(',')

        return self.__cache

    @pynvim.function('_fzf_gitignore_create', sync=True)
    def create(self, args):
        data = self.__fetch(','.join(args[0]))
        return data.split('\n')

# vim: ts=4 et sw=4
