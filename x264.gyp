{
	'variables':{
		#'library' : 'static_library',
		'library' : 'shared_library',
		'high_bit_depth' : '0',
		
		'yasm_output_path': '<(INTERMEDIATE_DIR)',
	},
	'target_defaults': {
		
		'msvs_settings': {
			# This magical incantation is necessary because VC++ will compile
			# object files to same directory... even if they have the same name!
			'VCCLCompilerTool': {
			  'ObjectFile': '$(IntDir)/%(RelativeDir)/',
			  'AdditionalOptions': ['/w']
			},
		},
		'configurations':{
			'Debug':{
				'msvs_settings':{
					'VCLinkerTool': {
						'GenerateDebugInformation': 'true',
					},
				},
			},
			'Release':{},
		},
		'conditions': [
			['OS=="linux" and target_arch=="ia32"',{
				'cflags':[
					'-m32',
				],
				'ldflags':[
					'-m32',
					'-L/usr/lib32',
					'-L/usr/lib32/debug',
				],
			}],
			['OS=="linux" and target_arch=="x64"',{
				'cflags':[
					'-m64'
				],
				'ldflags':[
					'-m64',
				],
			}],
		
			['OS == "win"',{
				'defines':[
					'__ICL',
					'inline=__inline',
					'__asm__=__asm',
				],
				'link_settings': {
					'libraries': [
						'-lShell32.lib',
					]
				 },
				 
			}],
			
			
			
			
		  ['OS != "win"', {
			'cflags':[
				'-std=gnu99',
			],
			
			'conditions': [
				['library == "shared_library"',{
					'cflags':[
						'-fPIC',
						'-Wno-maybe-uninitialized',
						 '-fomit-frame-pointer',
						 '-fno-tree-vectorize',
					],
					'ldflags':[
						'-Wl,-Bsymbolic',
					],
				}],
			  ['OS=="solaris"', {
				'cflags': [ '-pthreads' ],
			  }],
			  ['OS not in "solaris android"', {
				'ldflags':[
					'-pthread',
					'-lm',
					'-ldl',
				],
			  }],
			  ['OS=="android"',{
				'defines':[
					'ANDROID'
				],
			  }],
			],
		  }],
		],
	  },
	'targets':
	[
		{
			'target_name': 'x264',
			'type':'<(library)',
			
			'defines':[
				'HAVE_CONFIG_H',
			],
			
			'include_dirs':[
				'x264_src',
				'config/<(OS)/',
				'config',
			],
			'direct_dependent_settings': {
				'include_dirs': [
					'x264_src',
					'config/<(OS)/',
					'config',
				],
				'conditions':[
					['OS == "win" and library == "shared_library"',{
						'defines':[
							'X264_API_IMPORTS'
						],
					}],
				],
			 },
			'sources':[
				'x264_src/common/mc.c',
				'x264_src/common/predict.c',
				'x264_src/common/pixel.c',
				'x264_src/common/macroblock.c',
				'x264_src/common/frame.c',
				'x264_src/common/dct.c',
				'x264_src/common/cpu.c',
				'x264_src/common/cabac.c',
				'x264_src/common/common.c',
				'x264_src/common/osdep.c',
				'x264_src/common/rectangle.c',
				'x264_src/common/set.c',
				'x264_src/common/threadpool.c',
				'x264_src/common/quant.c',
				'x264_src/common/deblock.c', 
				'x264_src/common/vlc.c',
				'x264_src/common/mvpred.c',
				'x264_src/common/bitstream.c',
				'x264_src/encoder/analyse.c',
				'x264_src/encoder/me.c',
				'x264_src/encoder/ratecontrol.c',
				'x264_src/encoder/set.c',
				'x264_src/encoder/macroblock.c',
				'x264_src/encoder/cabac.c',
				'x264_src/encoder/cavlc.c',
				'x264_src/encoder/encoder.c',
				'x264_src/encoder/lookahead.c',			
			],
			
			'conditions':[
				['OS == "linux"',{
					'sources':[
						
					],
				}],
				['target_arch in "ia32 x64"',{
					
					'includes':[
						'yasm_compile.gypi',
					],
					'variables':{
						'yasm_flags':[
							'-DHIGH_BIT_DEPTH=<(high_bit_depth)',
							'-DBIT_DEPTH=8',
							'-DSTACK_ALIGNMENT=32',
						],
						'conditions':[
							['library == "shared_library"',{
								'yasm_flags':[
									'-DPIC',
								],
							}],
						],
					},
					'sources':[
						'x264_src/common/x86/mc-c.c',
						'x264_src/common/x86/predict-c.c',
						
						'x264_src/common/x86/x86inc.asm',
						'x264_src/common/x86/x86util.asm',
						
						'x264_src/common/x86/const-a.asm',
						'x264_src/common/x86/cabac-a.asm',
						'x264_src/common/x86/dct-a.asm',
						'x264_src/common/x86/deblock-a.asm',
						'x264_src/common/x86/mc-a.asm',
						'x264_src/common/x86/mc-a2.asm',
						'x264_src/common/x86/pixel-a.asm',
						'x264_src/common/x86/predict-a.asm',
						'x264_src/common/x86/quant-a.asm',
						'x264_src/common/x86/cpu-a.asm',
						
						'x264_src/common/x86/bitstream-a.asm',
						
						
					],
					
					'conditions':[
						['high_bit_depth == 1',{
							'sources':[
								'x264_src/common/x86/sad16-a.asm'
							],
						},{
							'sources':[
								'x264_src/common/x86/sad-a.asm',
							],
						}]
					],
					
				}],
				['target_arch == "ia32"',{
					'defines':[
						'ARCH_X86=1'
					],
					'sources':[
						'x264_src/common/x86/dct-32.asm',
						'x264_src/common/x86/pixel-32.asm',		
					],
				}],
				['target_arch == "x64"',{
					'defines':[
						'ARCH_X86_64=1'
					],
					'sources':[
						'x264_src/common/x86/trellis-64.asm',
						'x264_src/common/x86/dct-64.asm',
					],
				}],
				
				['target_arch == "ppc"',{
					'sources':[
						'x264_src/common/ppc/mc.c',
						'x264_src/common/ppc/pixel.c',
						'x264_src/common/ppc/dct.c',
						'x264_src/common/ppc/quant.c',
						'x264_src/common/ppc/deblock.c',
						'x264_src/common/ppc/predict.c',
					],

				}],
				
				['target_arch == "arm"',{
					'sources':[
						'x264_src/common/arm/mc-c.c',
						'x264_src/common/arm/predict-c.c',
						'x264_src/common/arm/cpu-a.S',
						'x264_src/common/arm/pixel-a.S',
						'x264_src/common/arm/mc-a.S',
						'x264_src/common/arm/dct-a.S',
						'x264_src/common/arm/quant-a.S',
						'x264_src/common/arm/deblock-a.S',
						'x264_src/common/arm/predict-a.S',
					],
				}],
				
				['OS == "win"',{
					'include_dirs':[
						'x264_src/extras'
					],
					
					'sources':[
						'x264_src/common/win32thread.c',
					],
					'conditions' : [
						['library == "shared_library"',{
							'sources':[
								'x264_src/x264dll.c',
								'x264_src/x264res.rc',
								'x264.def',
							],
						}],
					],
				}],
				
				
			],
		},
		{
			'target_name': 'x264cli',
			'type':'executable',
			'dependencies':[
				'x264',
			],
			
			'defines':[
				'HAVE_CONFIG_H',
			],

			'sources':[
				'x264_src/x264.c',
				'x264_src/input/input.c',
				'x264_src/input/timecode.c',
				'x264_src/input/raw.c',
				'x264_src/input/y4m.c',
				#'x264_src/input/avs.c',
				'x264_src/input/thread.c',
				#'x264_src/input/lavf.c',
				#'x264_src/input/ffms.c',
				'x264_src/output/raw.c',
				'x264_src/output/matroska.c',
				'x264_src/output/matroska_ebml.c',
				#'x264_src/output/mp4.c',
				#'x264_src/output/mp4_lsmash.c',
				'x264_src/output/flv.c',
				'x264_src/output/flv_bytestream.c',
				'x264_src/extras/getopt.c',
				'x264_src/filters/filters.c',
				'x264_src/filters/video/video.c',
				'x264_src/filters/video/source.c',
				'x264_src/filters/video/internal.c',
				'x264_src/filters/video/resize.c',
				'x264_src/filters/video/cache.c',
				'x264_src/filters/video/fix_vfr_pts.c',
				'x264_src/filters/video/select_every.c',
				'x264_src/filters/video/crop.c',
				'x264_src/filters/video/depth.c',				
			],
			'conditions':[
				['OS == "win"',{
					'include_dirs':[
						'x264_src/extras'
					],
				}],
			],
		}
	]
}