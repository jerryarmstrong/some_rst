clang/test/CodeGen/debug-info-renderscript-tag.rs
=================================================

Last edited: 2023-03-17 20:18:30

Contents:

.. code-block:: rs

    // RUN: %clang -emit-llvm -S -g %s -o - | FileCheck %s

// CHECK: !DICompileUnit(language: DW_LANG_GOOGLE_RenderScript{{.*}})


