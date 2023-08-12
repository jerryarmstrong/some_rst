testsuite/src/services_impl/validator/http_sender.rs
====================================================

Last edited: 2021-03-14 22:40:05

Contents:

.. code-block:: rs

    use anyhow::{anyhow, Result};
use log::*;
use reqwest::{StatusCode, blocking::Client, header::CONTENT_TYPE};
use serde_json::Value;
use std::{thread::sleep, time::Duration};

/*
NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE
This entire file is copied from https://github.com/solana-labs/solana/blob/master/client/src/rpc_request.rs
because solana-client provides Ledger support, which means it has a dependency
on the 'hidapi' kernel module. This module won't compile under Docker-for-Mac
due to https://github.com/docker/for-mac/issues/5295
Therefore, we reimplement parts of the Solana client here as a hackaround
NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE
*/

use super::{rpc_request::RpcRequest, rpc_sender::RpcSender};

const REQUEST_TIMEOUT: Duration = Duration::from_secs(30);

pub struct HttpSender {
    client: Client,
    url: String,
}

impl HttpSender {
    pub fn new(url: String) -> Self {
        Self::new_with_timeout(url, REQUEST_TIMEOUT)
    }

    pub fn new_with_timeout(url: String, timeout: Duration) -> Self {
        let client = Client::builder()
            .timeout(timeout)
            .build()
            .expect("build rpc client");

        Self { client, url }
    }
}

impl RpcSender for HttpSender {
    fn send(&self, request: RpcRequest, params: Value) -> Result<Value> {
        // Concurrent requests are not supported so reuse the same request id for all requests
        let request_id = 1;

        let request_json = request.build_request_json(request_id, params);

        let mut too_many_requests_retries = 5;
        loop {
            let resp_or_err = self.client
                .post(&self.url)
                .header(CONTENT_TYPE, "application/json")
                .body(request_json.to_string())
                .send();
            match resp_or_err
            {
                Ok(response) => {
                    if !response.status().is_success() {
                        if response.status() == StatusCode::TOO_MANY_REQUESTS
                            && too_many_requests_retries > 0
                        {
                            too_many_requests_retries -= 1;
                            debug!(
                                "Server responded with {:?}, {} retries left",
                                response, too_many_requests_retries
                            );

                            // Sleep for 500ms to give the server a break
                            sleep(Duration::from_millis(500));
                            continue;
                        }
                        return Err(response.error_for_status().unwrap_err().into());
                    }

                    let resp_body = response.text()?;
                    let json: Value = serde_json::from_str(&resp_body)?;
                    if json["error"].is_object() {
                        return Err(anyhow!(
                            "An error occurred making the JSON RPC request: {}",
                            json["error"].clone(),
                        ));
                    }
                    return Ok(json["result"].clone());
                }
                Err(err) => {
                    return Err(err.into());
                }
            }
        }
    }
}


