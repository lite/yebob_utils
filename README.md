yebob_utils
===========

	./src/main.py <app_url_in_market>
			<app_url_in_market> is the app url in market or app store

	market lists:

	+ itunes.apple.com
	http://itunes.apple.com/cn/genre/ios-you-xi/id6014?mt=8
	http://itunes.apple.com/cn/app/toca-robot-lab/id434826169?mt=8

	+ play.google.com
	https://play.google.com/store/apps/category/GAME/collection/topselling_free?hl=zh_CN
	https://play.google.com/store/apps/details?id=com.catstudio.soldierofglorycnzh
	https://play.google.com/store/apps/developer?id=GoodTeam

	+ 51ipa.com
	http://www.51ipa.com/games/rpg/
	http://www.51ipa.com/games/rpg/PiPHero-iPhone.html

	- d.cn
	http://android.d.cn/game/
	http://android.d.cn/game/rpg_0_all_all_update_7/
	http://android.d.cn/game/8213.html
	http://ios.d.cn/apps/games.html
	http://ios.d.cn/apps/iphone-games--------list-2.html
	http://ios.d.cn/apps/Fast+Five+the+Movie%3a+Official+Game-5466.html
	http://wp.d.cn/app/game/
	http://wp.d.cn/app/game/____2_.html
	http://wp.d.cn/app/slg/16845_radiant+defense.html

	+ windowsphone.com
	http://www.windowsphone.com/zh-CN/categories/actionandadventure?list=top
	http://www.windowsphone.com/zh-CN/publishers/Hexage
	http://www.windowsphone.com/zh-CN/apps/4a9e9b87-ccd8-4c95-8eef-846bfadc6e1e

Config
====

Add these to /etc/hosts
    203.208.46.30 lh1.ggpht.com
    203.208.46.30 lh2.ggpht.com
    203.208.46.30 lh3.ggpht.com
    203.208.46.30 lh4.ggpht.com
    203.208.46.30 lh5.ggpht.com
    203.208.46.30 lh6.ggpht.com

Then 

    cp ./conf/config.yaml.example ./conf/config.yaml
    pip install virtualenv
    pip install virtualenvwrapper
    pip freeze > requirements.txt
    pip install -r requirements.txt
    workon yebob

Then fill your yebob username and password in config.yaml

Test
====

	nosetests -w . ./test
	nosetests -w . ./test/test_YebobDoc.py
	python test/test_YebobDoc.py

TBD
====

    Name should less 60 Bytes    

Thanks
====

+ [nose](https://github.com/nose-devs/nose)
+ [PyYAML](http://pyyaml.org/wiki/PyYAMLDocumentation)
+ [Mechanize](http://wwwsearch.sourceforge.net/mechanize/)
+ [BeautifulSoup4](http://www.crummy.com/software/BeautifulSoup/bs4/doc/)
+ [html5lib](https://code.google.com/p/html5lib/wiki/UserDocumentation)
+ [html2text](https://github.com/aaronsw/html2text/)
