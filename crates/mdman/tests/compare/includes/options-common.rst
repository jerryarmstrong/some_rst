crates/mdman/tests/compare/includes/options-common.md
=====================================================

Last edited: 2023-03-17 21:53:33

Contents:

.. code-block:: md

    {{#options}}
{{#option "`@`_filename_"}}
Load from filename.
{{/option}}

{{#option "`--foo` [_bar_]"}}
Flag with optional value.
{{/option}}

{{#option "`--foo`[`=`_bar_]"}}
Alternate syntax for optional value (with required = for disambiguation).
{{/option}}

{{/options}}


