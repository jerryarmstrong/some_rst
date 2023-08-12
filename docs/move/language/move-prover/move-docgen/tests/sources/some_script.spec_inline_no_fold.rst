language/move-prover/move-docgen/tests/sources/some_script.spec_inline_no_fold.md
=================================================================================

Last edited: 2023-08-11 19:18:44

Contents:

.. code-block:: md

    
<a name="some"></a>

# Script `some`





<pre><code></code></pre>


This script does really nothing but just aborts.


<pre><code><b>public</b> <b>fun</b> <a href="some_script.md#some">some</a>&lt;T&gt;(_account: signer)
</code></pre>



##### Implementation


<pre><code><b>fun</b> <a href="some_script.md#some">some</a>&lt;T&gt;(_account: signer) {
    <b>abort</b> 1
}
</code></pre>


