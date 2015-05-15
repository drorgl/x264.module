# x264 GYP Module

** Experimental **

expose x264 through gyp

- can be used stand alone to compile x264 as static/shared libraries ( / dll) 
	static/shared library can be changed in the variables section of x264.gyp
- can be used as part of a bigger gyp project (which was the original intent) :

```
'dependencies':[
	'x264.module/x264.gyp:x264'
]
```

x264 source git://git.videolan.org/x264.git
x264 licensing http://x264licensing.com/

Please note that x264 is dual licensed GPL and commercial, see http://x264licensing.com/faq

I'm in no way associated with x264/VideoLAN.

```
gyp x264.gyp -DOS=win -Dtarget_arch=ia32 -Duse_system_yasm=0 --depth=. -f msvs -G msvs_version=2013 --generator-output=./build.vs2013/

gyp x264.gyp -DOS=win -Dtarget_arch=x64 -Duse_system_yasm=0 --depth=. -f msvs -G msvs_version=2013 --generator-output=./build.vs2013/

gyp x264.gyp -DOS=linux -Dtarget_arch=ia32 -Duse_system_yasm=1 --depth=. -f make --generator-output=./build.linux32/

gyp x264.gyp -DOS=linux -Dtarget_arch=x64 -Duse_system_yasm=1 --depth=. -f make --generator-output=./build.linux64/

gyp x264.gyp -DOS=android -Dtarget_arch=arm --depth=. -f make --generator-output=./build.android/
```

x264 requires yasm > 1.3
I've used this command on my old Ubuntu 12:
```
wget https://launchpad.net/~mc3man/+archive/ubuntu/media-1/+build/6676721/+files/yasm_1.3.0-1~trusty_amd64.deb -O  /var/cache/apt/archives/yasm_1.3.0-1~trusty_amd64.deb
dpkg /var/cache/apt/archives/yasm_1.3.0-1~trusty_amd64.deb
```
