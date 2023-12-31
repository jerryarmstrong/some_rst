compiler/rustc_target/src/asm/wasm.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use super::{InlineAsmArch, InlineAsmType};
use rustc_macros::HashStable_Generic;
use rustc_span::Symbol;

def_reg_class! {
    Wasm WasmInlineAsmRegClass {
        local,
    }
}

impl WasmInlineAsmRegClass {
    pub fn valid_modifiers(self, _arch: super::InlineAsmArch) -> &'static [char] {
        &[]
    }

    pub fn suggest_class(self, _arch: InlineAsmArch, _ty: InlineAsmType) -> Option<Self> {
        None
    }

    pub fn suggest_modifier(
        self,
        _arch: InlineAsmArch,
        _ty: InlineAsmType,
    ) -> Option<(char, &'static str)> {
        None
    }

    pub fn default_modifier(self, _arch: InlineAsmArch) -> Option<(char, &'static str)> {
        None
    }

    pub fn supported_types(
        self,
        _arch: InlineAsmArch,
    ) -> &'static [(InlineAsmType, Option<Symbol>)] {
        match self {
            Self::local => {
                types! { _: I8, I16, I32, I64, F32, F64; }
            }
        }
    }
}

def_regs! {
    // WebAssembly doesn't have registers.
    Wasm WasmInlineAsmReg WasmInlineAsmRegClass {}
}


