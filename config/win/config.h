#define ARCH_ARM 0
#define SYS_LINUX 0
#define SYS_CYGWIN 0
#define SYS_WINDOWS 1

//#define STACK_ALIGNMENT 4

//#define ARCH_X86 (1)
//#define ARCH_X86_64 1

#define HAVE_AVS 1
#define HAVE_AS_FUNC 0
#define HAVE_INTEL_DISPATCHER 0
#define HAVE_VECTOREXT 1
#define HAVE_LOG2F 1
#define HAVE_WIN32THREAD 1
#define HAVE_THREAD 1
#define USE_AVXSYNTH 0
#define HAVE_INTERLACED 1
#define HAVE_OPENCL 0
#define HAVE_MALLOC_H 0
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

#define X264_MPEG2 1
#define X264_POINTVER ""


#define HAVE_GPL 1

#define HAVE_X86_INLINE_ASM 0


//SSE2 throws access violation in VS2013, for now its disabled
#define HAVE_MMX 1
#define HAVE_STRING_H 1