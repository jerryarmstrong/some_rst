src/tools/rustfmt/tests/target/issue-2927.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-edition: 2018
#![feature(rust_2018_preview, uniform_paths)]
use ::log::{error, info, log};
use futures::prelude::*;
use http_03::cli::Cli;
use hyper::{service::service_fn_ok, Body, Response, Server};
use structopt::StructOpt;


