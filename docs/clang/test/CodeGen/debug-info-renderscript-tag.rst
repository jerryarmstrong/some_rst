test/CodeGen/debug-info-renderscript-tag.rs
===========================================

Last edited: 2018-11-26 16:38:37

Contents:

.. code-block:: rs

    // RUN: %clang -emit-llvm -S -g %s -o - | FileCheck %s

// CHECK: !DICompileUnit(language: DW_LANG_GOOGLE_RenderScript{{.*}})


