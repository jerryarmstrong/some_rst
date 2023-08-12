testsuite/src/services_impl/faucet/faucet_service.rs
====================================================

Last edited: 2021-03-14 22:40:05

Contents:

.. code-block:: rs

    use kurtosis_rust_lib::services::{service::Service, service_context::ServiceContext};

pub (super) const FAUCET_PORT: u32 = 9900;

pub struct FaucetService {
    service_context: ServiceContext,
    keypair_json: String,
}

impl FaucetService {
    pub fn new(service_context: ServiceContext, keypair_json: String) -> FaucetService {
        return FaucetService{
            service_context,
            keypair_json,
        };
    }

    pub fn get_ip_address(&self) -> &str {
        return self.service_context.get_ip_address();
    }

    pub fn get_port(&self) -> u32 {
        return FAUCET_PORT;
    }

    pub fn get_keypair_json(&self) -> String {
        return self.keypair_json.clone();
    }
}

impl Service for FaucetService {
    fn is_available(&self) -> bool {
        // Faucet operates on UDP - no guarantees of availability
        return true;
    }
}

