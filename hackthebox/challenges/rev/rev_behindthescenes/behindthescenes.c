typedef unsigned char   undefined;

typedef unsigned char    byte;
typedef unsigned char    dwfenc;
typedef unsigned int    dword;
typedef unsigned long    qword;
typedef unsigned int    uint;
typedef unsigned long    ulong;
typedef unsigned char    undefined1;
typedef unsigned int    undefined4;
typedef unsigned long    undefined8;
typedef unsigned short    word;
typedef struct eh_frame_hdr eh_frame_hdr, *Peh_frame_hdr;

struct eh_frame_hdr {
    byte eh_frame_hdr_version; // Exception Handler Frame Header Version
    dwfenc eh_frame_pointer_encoding; // Exception Handler Frame Pointer Encoding
    dwfenc eh_frame_desc_entry_count_encoding; // Encoding of # of Exception Handler FDEs
    dwfenc eh_frame_table_encoding; // Exception Handler Table Encoding
};

typedef struct NoteGnuPropertyElement_4 NoteGnuPropertyElement_4, *PNoteGnuPropertyElement_4;

struct NoteGnuPropertyElement_4 {
    dword prType;
    dword prDatasz;
    byte data[4];
};

typedef struct fde_table_entry fde_table_entry, *Pfde_table_entry;

struct fde_table_entry {
    dword initial_loc; // Initial Location
    dword data_loc; // Data location
};

typedef union _union_1457 _union_1457, *P_union_1457;

typedef struct siginfo siginfo, *Psiginfo;

typedef struct siginfo siginfo_t;

typedef void (* __sighandler_t)(int);

typedef union _union_1441 _union_1441, *P_union_1441;

typedef struct _struct_1442 _struct_1442, *P_struct_1442;

typedef struct _struct_1443 _struct_1443, *P_struct_1443;

typedef struct _struct_1444 _struct_1444, *P_struct_1444;

typedef struct _struct_1445 _struct_1445, *P_struct_1445;

typedef struct _struct_1446 _struct_1446, *P_struct_1446;

typedef struct _struct_1447 _struct_1447, *P_struct_1447;

typedef int __pid_t;

typedef uint __uid_t;

typedef union sigval sigval, *Psigval;

typedef union sigval sigval_t;

typedef long __clock_t;

struct _struct_1445 {
    __pid_t si_pid;
    __uid_t si_uid;
    int si_status;
    __clock_t si_utime;
    __clock_t si_stime;
};

union sigval {
    int sival_int;
    void * sival_ptr;
};

struct _struct_1444 {
    __pid_t si_pid;
    __uid_t si_uid;
    sigval_t si_sigval;
};

struct _struct_1443 {
    int si_tid;
    int si_overrun;
    sigval_t si_sigval;
};

struct _struct_1446 {
    void * si_addr;
};

struct _struct_1447 {
    long si_band;
    int si_fd;
};

struct _struct_1442 {
    __pid_t si_pid;
    __uid_t si_uid;
};

union _union_1441 {
    int _pad[28];
    struct _struct_1442 _kill;
    struct _struct_1443 _timer;
    struct _struct_1444 _rt;
    struct _struct_1445 _sigchld;
    struct _struct_1446 _sigfault;
    struct _struct_1447 _sigpoll;
};

union _union_1457 {
    __sighandler_t sa_handler;
    void (* sa_sigaction)(int, siginfo_t *, void *);
};

struct siginfo {
    int si_signo;
    int si_errno;
    int si_code;
    union _union_1441 _sifields;
};

typedef struct sigaction sigaction, *Psigaction;

typedef struct __sigset_t __sigset_t, *P__sigset_t;

struct __sigset_t {
    ulong __val[16];
};

struct sigaction {
    union _union_1457 __sigaction_handler;
    struct __sigset_t sa_mask;
    int sa_flags;
    void (* sa_restorer)(void);
};

typedef ulong size_t;

typedef struct __sigset_t sigset_t;

typedef struct evp_pkey_ctx_st evp_pkey_ctx_st, *Pevp_pkey_ctx_st;

typedef struct evp_pkey_ctx_st EVP_PKEY_CTX;

struct evp_pkey_ctx_st {
};

typedef enum Elf_ProgramHeaderType {
    PT_NULL=0,
    PT_LOAD=1,
    PT_DYNAMIC=2,
    PT_INTERP=3,
    PT_NOTE=4,
    PT_SHLIB=5,
    PT_PHDR=6,
    PT_TLS=7,
    PT_GNU_EH_FRAME=1685382480,
    PT_GNU_STACK=1685382481,
    PT_GNU_RELRO=1685382482
} Elf_ProgramHeaderType;

typedef struct Elf64_Shdr Elf64_Shdr, *PElf64_Shdr;

typedef enum Elf_SectionHeaderType {
    SHT_NULL=0,
    SHT_PROGBITS=1,
    SHT_SYMTAB=2,
    SHT_STRTAB=3,
    SHT_RELA=4,
    SHT_HASH=5,
    SHT_DYNAMIC=6,
    SHT_NOTE=7,
    SHT_NOBITS=8,
    SHT_REL=9,
    SHT_SHLIB=10,
    SHT_DYNSYM=11,
    SHT_INIT_ARRAY=14,
    SHT_FINI_ARRAY=15,
    SHT_PREINIT_ARRAY=16,
    SHT_GROUP=17,
    SHT_SYMTAB_SHNDX=18,
    SHT_ANDROID_REL=1610612737,
    SHT_ANDROID_RELA=1610612738,
    SHT_GNU_ATTRIBUTES=1879048181,
    SHT_GNU_HASH=1879048182,
    SHT_GNU_LIBLIST=1879048183,
    SHT_CHECKSUM=1879048184,
    SHT_SUNW_move=1879048186,
    SHT_SUNW_COMDAT=1879048187,
    SHT_SUNW_syminfo=1879048188,
    SHT_GNU_verdef=1879048189,
    SHT_GNU_verneed=1879048190,
    SHT_GNU_versym=1879048191
} Elf_SectionHeaderType;

struct Elf64_Shdr {
    dword sh_name;
    enum Elf_SectionHeaderType sh_type;
    qword sh_flags;
    qword sh_addr;
    qword sh_offset;
    qword sh_size;
    dword sh_link;
    dword sh_info;
    qword sh_addralign;
    qword sh_entsize;
};

typedef struct Elf64_Dyn Elf64_Dyn, *PElf64_Dyn;

typedef enum Elf64_DynTag {
    DT_NULL=0,
    DT_NEEDED=1,
    DT_PLTRELSZ=2,
    DT_PLTGOT=3,
    DT_HASH=4,
    DT_STRTAB=5,
    DT_SYMTAB=6,
    DT_RELA=7,
    DT_RELASZ=8,
    DT_RELAENT=9,
    DT_STRSZ=10,
    DT_SYMENT=11,
    DT_INIT=12,
    DT_FINI=13,
    DT_SONAME=14,
    DT_RPATH=15,
    DT_SYMBOLIC=16,
    DT_REL=17,
    DT_RELSZ=18,
    DT_RELENT=19,
    DT_PLTREL=20,
    DT_DEBUG=21,
    DT_TEXTREL=22,
    DT_JMPREL=23,
    DT_BIND_NOW=24,
    DT_INIT_ARRAY=25,
    DT_FINI_ARRAY=26,
    DT_INIT_ARRAYSZ=27,
    DT_FINI_ARRAYSZ=28,
    DT_RUNPATH=29,
    DT_FLAGS=30,
    DT_PREINIT_ARRAY=32,
    DT_PREINIT_ARRAYSZ=33,
    DT_RELRSZ=35,
    DT_RELR=36,
    DT_RELRENT=37,
    DT_ANDROID_REL=1610612751,
    DT_ANDROID_RELSZ=1610612752,
    DT_ANDROID_RELA=1610612753,
    DT_ANDROID_RELASZ=1610612754,
    DT_ANDROID_RELR=1879040000,
    DT_ANDROID_RELRSZ=1879040001,
    DT_ANDROID_RELRENT=1879040003,
    DT_GNU_PRELINKED=1879047669,
    DT_GNU_CONFLICTSZ=1879047670,
    DT_GNU_LIBLISTSZ=1879047671,
    DT_CHECKSUM=1879047672,
    DT_PLTPADSZ=1879047673,
    DT_MOVEENT=1879047674,
    DT_MOVESZ=1879047675,
    DT_FEATURE_1=1879047676,
    DT_POSFLAG_1=1879047677,
    DT_SYMINSZ=1879047678,
    DT_SYMINENT=1879047679,
    DT_GNU_XHASH=1879047924,
    DT_GNU_HASH=1879047925,
    DT_TLSDESC_PLT=1879047926,
    DT_TLSDESC_GOT=1879047927,
    DT_GNU_CONFLICT=1879047928,
    DT_GNU_LIBLIST=1879047929,
    DT_CONFIG=1879047930,
    DT_DEPAUDIT=1879047931,
    DT_AUDIT=1879047932,
    DT_PLTPAD=1879047933,
    DT_MOVETAB=1879047934,
    DT_SYMINFO=1879047935,
    DT_VERSYM=1879048176,
    DT_RELACOUNT=1879048185,
    DT_RELCOUNT=1879048186,
    DT_FLAGS_1=1879048187,
    DT_VERDEF=1879048188,
    DT_VERDEFNUM=1879048189,
    DT_VERNEED=1879048190,
    DT_VERNEEDNUM=1879048191,
    DT_AUXILIARY=2147483645,
    DT_FILTER=2147483647
} Elf64_DynTag;

struct Elf64_Dyn {
    enum Elf64_DynTag d_tag;
    qword d_val;
};

typedef struct GnuBuildId GnuBuildId, *PGnuBuildId;

struct GnuBuildId {
    dword namesz; // Length of name field
    dword descsz; // Length of description field
    dword type; // Vendor specific type
    char name[4]; // Vendor name
    byte hash[20];
};

typedef struct NoteGnuProperty_4 NoteGnuProperty_4, *PNoteGnuProperty_4;

struct NoteGnuProperty_4 {
    dword namesz; // Length of name field
    dword descsz; // Length of description field
    dword type; // Vendor specific type
    char name[4]; // Vendor name
};

typedef struct Elf64_Ehdr Elf64_Ehdr, *PElf64_Ehdr;

struct Elf64_Ehdr {
    byte e_ident_magic_num;
    char e_ident_magic_str[3];
    byte e_ident_class;
    byte e_ident_data;
    byte e_ident_version;
    byte e_ident_osabi;
    byte e_ident_abiversion;
    byte e_ident_pad[7];
    word e_type;
    word e_machine;
    dword e_version;
    qword e_entry;
    qword e_phoff;
    qword e_shoff;
    dword e_flags;
    word e_ehsize;
    word e_phentsize;
    word e_phnum;
    word e_shentsize;
    word e_shnum;
    word e_shstrndx;
};

typedef struct Elf64_Rela Elf64_Rela, *PElf64_Rela;

struct Elf64_Rela {
    qword r_offset; // location to apply the relocation action
    qword r_info; // the symbol table index and the type of relocation
    qword r_addend; // a constant addend used to compute the relocatable field value
};

typedef struct Elf64_Sym Elf64_Sym, *PElf64_Sym;

struct Elf64_Sym {
    dword st_name;
    byte st_info;
    byte st_other;
    word st_shndx;
    qword st_value;
    qword st_size;
};

typedef struct Elf64_Phdr Elf64_Phdr, *PElf64_Phdr;

struct Elf64_Phdr {
    enum Elf_ProgramHeaderType p_type;
    dword p_flags;
    qword p_offset;
    qword p_vaddr;
    qword p_paddr;
    qword p_filesz;
    qword p_memsz;
    qword p_align;
};

typedef struct NoteAbiTag NoteAbiTag, *PNoteAbiTag;

struct NoteAbiTag {
    dword namesz; // Length of name field
    dword descsz; // Length of description field
    dword type; // Vendor specific type
    char name[4]; // Vendor name
    dword abiType; // 0 == Linux
    dword requiredKernelVersion[3]; // Major.minor.patch
};




int _init(EVP_PKEY_CTX *ctx)

{
  int iVar1;
  
  iVar1 = __gmon_start__();
  return iVar1;
}



void FUN_00101020(void)

{
                    // WARNING: Treating indirect jump as call
  (*(code *)(undefined *)0x0)();
  return;
}



void __cxa_finalize(void)

{
  __cxa_finalize();
  return;
}



// WARNING: Unknown calling convention -- yet parameter storage is locked

int strncmp(char *__s1,char *__s2,size_t __n)

{
  int iVar1;
  
  iVar1 = strncmp(__s1,__s2,__n);
  return iVar1;
}



// WARNING: Unknown calling convention -- yet parameter storage is locked

int sigaction(int __sig,sigaction *__act,sigaction *__oact)

{
  int iVar1;
  
  iVar1 = sigaction(__sig,__act,__oact);
  return iVar1;
}



// WARNING: Unknown calling convention -- yet parameter storage is locked

void * memset(void *__s,int __c,size_t __n)

{
  void *pvVar1;
  
  pvVar1 = memset(__s,__c,__n);
  return pvVar1;
}



// WARNING: Unknown calling convention -- yet parameter storage is locked

int sigemptyset(sigset_t *__set)

{
  int iVar1;
  
  iVar1 = sigemptyset(__set);
  return iVar1;
}



void processEntry _start(undefined8 param_1,undefined8 param_2)

{
  undefined auStack_8 [8];
  
  __libc_start_main(main,param_2,&stack0x00000008,__libc_csu_init,__libc_csu_fini,param_1,auStack_8)
  ;
  do {
                    // WARNING: Do nothing block with infinite loop
  } while( true );
}



// WARNING: Removing unreachable block (ram,0x00101183)
// WARNING: Removing unreachable block (ram,0x0010118f)

void deregister_tm_clones(void)

{
  return;
}



// WARNING: Removing unreachable block (ram,0x001011c4)
// WARNING: Removing unreachable block (ram,0x001011d0)

void register_tm_clones(void)

{
  return;
}



void __do_global_dtors_aux(void)

{
  if (completed_8060 != '\0') {
    return;
  }
  __cxa_finalize(__dso_handle);
  deregister_tm_clones();
  completed_8060 = 1;
  return;
}



void frame_dummy(void)

{
  register_tm_clones();
  return;
}



void segill_sigaction(undefined8 param_1,undefined8 param_2,long param_3)

{
  *(long *)(param_3 + 0xa8) = *(long *)(param_3 + 0xa8) + 2;
  return;
}



void main(void)

{
  long in_FS_OFFSET;
  sigaction local_a8;
  undefined8 canary;
  
  canary = *(undefined8 *)(in_FS_OFFSET + 0x28);
  memset(&local_a8,0,0x98);
  sigemptyset(&local_a8.sa_mask);
  local_a8.__sigaction_handler.sa_handler = segill_sigaction;
  local_a8.sa_flags = 4;
  sigaction(4,&local_a8,(sigaction *)0x0);
  do {
    invalidInstructionException();
  } while( true );
}



void __libc_csu_init(EVP_PKEY_CTX *param_1,undefined8 param_2,undefined8 param_3)

{
  long lVar1;
  
  _init(param_1);
  lVar1 = 0;
  do {
    (*(code *)(&__frame_dummy_init_array_entry)[lVar1])((ulong)param_1 & 0xffffffff,param_2,param_3)
    ;
    lVar1 = lVar1 + 1;
  } while (lVar1 != 1);
  return;
}



void __libc_csu_fini(void)

{
  return;
}



void _fini(void)

{
  return;
}


