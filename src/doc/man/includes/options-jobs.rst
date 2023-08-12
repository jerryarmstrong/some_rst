src/doc/man/includes/options-jobs.md
====================================

Last edited: 2023-03-17 21:53:33

Contents:

.. code-block:: md

    {{#option "`-j` _N_" "`--jobs` _N_"}}
Number of parallel jobs to run. May also be specified with the
`build.jobs` [config value](../reference/config.html). Defaults to
the number of logical CPUs. If negative, it sets the maximum number of
parallel jobs to the number of logical CPUs plus provided value.
Should not be 0.
{{/option}}


