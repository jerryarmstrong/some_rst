src/doc/unstable-book/src/language-features/debugger-visualizer.md
==================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: md

    # `debugger_visualizer`

The tracking issue for this feature is: [#95939]

[#95939]: https://github.com/rust-lang/rust/issues/95939

------------------------

The `debugger_visualizer` attribute can be used to instruct the compiler
to embed a debugger visualizer file into the PDB/ELF generated by `rustc`.

## Examples

``` rust,ignore (partial-example)
#![feature(debugger_visualizer)]
#![debugger_visualizer(natvis_file = "foo.natvis")]
#![debugger_visualizer(gdb_script_file = "foo.py")]
struct Foo {

}
```

## Limitations

Currently, this feature only supports embedding Natvis files on `-windows-msvc`
targets via the `natvis_file` meta item. `-windows-gnu` targets are not currently
supported.


