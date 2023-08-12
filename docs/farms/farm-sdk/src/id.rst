farm-sdk/src/id.rs
==================

Last edited: 2022-12-05 19:44:34

Contents:

.. code-block:: rs

    //! Official accounts and program ids

include!(concat!(
    env!(
        "OUT_DIR",
        "Please set OUT_DIR environment variable to the build script output path"
    ),
    "/constants.rs"
));


