src/ntnls.rs
============

Last edited: 2023-04-20 23:00:37

Contents:

.. code-block:: rs

    use winapi::shared::ntdef::{BOOLEAN, PUSHORT, PVOID, UCHAR, USHORT};
pub const MAXIMUM_LEADBYTES: usize = 12;
STRUCT!{struct CPTABLEINFO {
    CodePage: USHORT,
    MaximumCharacterSize: USHORT,
    DefaultChar: USHORT,
    UniDefaultChar: USHORT,
    TransDefaultChar: USHORT,
    TransUniDefaultChar: USHORT,
    DBCSCodePage: USHORT,
    LeadByte: [UCHAR; MAXIMUM_LEADBYTES],
    MultiByteTable: PUSHORT,
    WideCharTable: PVOID,
    DBCSRanges: PUSHORT,
    DBCSOffsets: PUSHORT,
}}
pub type PCPTABLEINFO = *mut CPTABLEINFO;
STRUCT!{struct NLSTABLEINFO {
    OemTableInfo: CPTABLEINFO,
    AnsiTableInfo: CPTABLEINFO,
    UpperCaseTable: PUSHORT,
    LowerCaseTable: PUSHORT,
}}
pub type PNLSTABLEINFO = *mut NLSTABLEINFO;
EXTERN!{extern "C" {
    static mut NlsAnsiCodePage: USHORT;
    static mut NlsMbCodePageTag: BOOLEAN;
    static mut NlsMbOemCodePageTag: BOOLEAN;
}}


