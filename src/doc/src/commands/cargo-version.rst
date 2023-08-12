src/doc/src/commands/cargo-version.md
=====================================

Last edited: 2023-03-17 21:53:33

Contents:

.. code-block:: md

    # cargo-version(1)

## NAME

cargo-version - Show version information

## SYNOPSIS

`cargo version` [_options_]

## DESCRIPTION

Displays the version of Cargo.

## OPTIONS

<dl>

<dt class="option-term" id="option-cargo-version--v"><a class="option-anchor" href="#option-cargo-version--v"></a><code>-v</code></dt>
<dt class="option-term" id="option-cargo-version---verbose"><a class="option-anchor" href="#option-cargo-version---verbose"></a><code>--verbose</code></dt>
<dd class="option-desc">Display additional version information.</dd>


</dl>

## EXAMPLES

1. Display the version:

       cargo version

2. The version is also available via flags:

       cargo --version
       cargo -V

3. Display extra version information:

       cargo -Vv

## SEE ALSO
[cargo(1)](cargo.html)


