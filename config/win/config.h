////#define ARCH_ARM (1)
////#define SYS_LINUX (1)
//
#define STACK_ALIGNMENT 32
//
//#define ARCH_X86 (1)
//
//#define HAVE_MALLOC_H (1)
////#define HAVE_ALTIVEC 
////#define HAVE_ALTIVEC_H 
//#define HAVE_MMX (1)
////#define HAVE_ARMV6 
////#define HAVE_ARMV6T2 
////#define HAVE_NEON 
////#define HAVE_BEOSTHREAD 
////#define HAVE_POSIXTHREAD (1)
//#define SYS_WINDOWS (1)
//#define HAVE_WIN32THREAD (1)
//#define HAVE_THREAD (1)
////#define HAVE_SWSCALE 
////#define HAVE_LAVF 
////#define HAVE_FFMS 
////#define HAVE_GPAC 
////#define HAVE_AVS 
//#define HAVE_GPL (1)
////#define HAVE_VECTOREXT 
//#define HAVE_INTERLACED (0)
//#define HAVE_CPU_COUNT (1)
//#define HAVE_OPENCL (0)
////#define HAVE_THP 
////#define HAVE_LSMASH

#define HAVE_LOG2F 1


#define SYS_WINDOWS 1
#define HAVE_WIN32THREAD 1
#define HAVE_THREAD 1
#define USE_AVXSYNTH 0
#define HAVE_VECTOREXT 1
#define HAVE_INTERLACED 1
#define HAVE_OPENCL 0
#define HAVE_MALLOC_H 1
#define HAVE_ALTIVEC 0
#define HAVE_ALTIVEC_H 0
#define HAVE_ARMV6 0
#define HAVE_ARMV6T2 0
#define HAVE_NEON 0
#define HAVE_BEOSTHREAD 0
#define HAVE_POSIXTHREAD 0
#define HAVE_SWSCALE 0
#define HAVE_LAVF 0
#define HAVE_FFMS 0
#define HAVE_GPAC 0
#define HAVE_CPU_COUNT 0
#define HAVE_THP 0
#define HAVE_LSMASH 0
#define HAVE_MPEG2 1
#define HAVE_STRING_H 1

//# VC headers cannot deal with fseek being redefined via macro to _fseeki64
//# It causes two conflicting funcdefs from stdio.h.x264 should probably use X264_FSEEK here
//#define fseek _fseeki64
//#define ftell _ftelli64

//#define X264_INTERLACED 1
//#define X264_CHROMA_FORMAT 0
#define X264_MPEG2 1
//#define X264_VERSION ""
#define X264_POINTVER ""


//#define X264_BIT_DEPTH 8 //or 10
//#define HIGH_BIT_DEPTH 0 //or 1

#define HAVE_GPL 1

//SSE2 throws access violation in VS2013, for now its disabled
#define HAVE_MMX 0

#define HAVE_STRING_H 1