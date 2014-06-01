# !/usr/bin/env python
# -*- coding: utf-8 -*-
# --------------------------------
# Copyright (c) 2014 "Zack Dibe" [http://www.zackdibe.com]

# This file is part of MigdalBavel.

# MigdalBavel is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# MigdalBavel is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with MigdalBavel.  If not, see <http://www.gnu.org/licenses/>.
# ---------------------------------

import praw

from ConfigParser import SafeConfigParser, ParsingError
from os import listdir
from os.path import isfile, join

import pprint

import time
import datetime

class MigdalBavel(object):
    class Config(object):
        def __init__(self, *args, **kwargs):
            super(MigdalBavel.Config, self).__init__(*args, **kwargs)

            self.config_parser = SafeConfigParser()


        def read(self, path):
            try:
                self.config_parser.read(path)

            except ParsingError as e:
                print("ERROR : - Could not read configuration file at %s. Now exiting" % path)
                raise e


        def get_section(self, section):
            return (dict(self.config_parser.items(section)))




    def __init__(self, *args, **kwargs):
        super(MigdalBavel, self).__init__(*args, **kwargs)

        self.config = MigdalBavel.Config()
        self.load_config("files/config/bot/")
        self.login_info = self.config.get_section("login")

        try:
            timestamp = datetime.datetime.fromtimestamp(time.time()).strftime("%Y%m%d%H%M%S")
            self.reddit = praw.Reddit(user_agent = self.login_info["user_agent"] + timestamp)
        except:
            print ("Error : - Could not initiate PRAW, wrong login section.")
            raise


    def login(self):
        if ("username" in self.login_info
            and "password" in self.login_info):
            print ("[+] Logging in as [%s] with password [%s]"
                   % (self.login_info["username"], self.login_info["password"]))
            self.reddit.login(self.login_info["username"], self.login_info["password"])
        else:
            print ("[-] Error : Could not log in, wrong login section.")


    def load_config(self, path):
        for f in listdir(path):
            if isfile(join(path,f)):
                self.config.read(join(path, f))




if __name__ == '__main__':
    bot = MigdalBavel()

    bot.login()
