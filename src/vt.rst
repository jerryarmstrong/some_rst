src/vt.rs
=========

Last edited: 2022-10-31 20:56:14

Contents:

.. code-block:: rs

    use super::*;
use crate::errors::VtError;

// Wrapper types.
#[derive(Serialize, Deserialize)]
pub struct Vm(pub VersionedMessage);

#[derive(Serialize, Deserialize)]
pub struct Vt(pub VersionedTransaction);

impl Deref for Vm {
    type Target = VersionedMessage;

    fn deref(&self) -> &Self::Target {
        &self.0
    }
}

impl Deref for Vt {
    type Target = VersionedTransaction;

    fn deref(&self) -> &Self::Target {
        &self.0
    }
}

pub struct VersionedMessageArgs {
    pub payer: Pubkey,
    pub instructions: Vec<Instruction>,
    pub address_luts: Vec<AddressLookupTableAccount>,
    pub latest_blockhash: Hash,
}

impl IntoVm for VersionedMessageArgs {
    fn into_vm(self) -> Result<Vm, VtError> {
        let vm = VersionedMessage::V0(
            Message::try_compile(
                &self.payer,
                &self.instructions,
                &self.address_luts,
                self.latest_blockhash,
            )
            .map_err(|e| VtError::ConversionError(format!("Failed to convert to Vm: {}", e)))?,
        );

        Ok(Vm(vm))
    }
}

impl Vm {
    pub fn new(args: VersionedMessageArgs) -> Result<Self, CompileError> {
        let vm = VersionedMessage::V0(Message::try_compile(
            &args.payer,
            &args.instructions,
            args.address_luts.as_slice(),
            args.latest_blockhash,
        )?);
        Ok(Self(vm))
    }
}

pub trait IntoVm {
    fn into_vm(self) -> Result<Vm, VtError>;
}

impl Vt {
    pub fn new<T: Sized + IntoVm>(vm: T, keypairs: Vec<Keypair>) -> Result<Vt, VtError> {
        let keypairs = &keypairs.iter().collect::<Vec<_>>();
        let vm = vm
            .into_vm()
            .map_err(|e| VtError::ConversionError(e.to_string()))?;

        let vt = VersionedTransaction::try_new(vm.0, keypairs).map_err(|e| {
            VtError::SignerError(format!(
                "Failed to sign transaction: {:?} with keypairs: {:?}",
                e, keypairs
            ))
        })?;

        Ok(Vt(vt))
    }

    pub fn sign_and_send(self, client: &RpcClient) -> Result<Signature, VtError> {
        let serialized_versioned_tx =
            bincode::serialize(&self).map_err(|e| VtError::SerializationError(e.to_string()))?;

        let serialized_encoded = base64::encode(serialized_versioned_tx);
        let rpc_config = RpcSendTransactionConfig {
            skip_preflight: false,
            preflight_commitment: Some(CommitmentLevel::Processed),
            encoding: Some(UiTransactionEncoding::Base64),
            ..RpcSendTransactionConfig::default()
        };

        // Have to do some manual RPC calls here because the v1.10 RPC client doesn't support
        // sending versioned transactions.

        let signature = client
            .send::<String>(
                RpcRequest::SendTransaction,
                json!([serialized_encoded, rpc_config]),
            )
            .map_err(|e| VtError::ClientError(e.to_string()))?;

        client
            .confirm_transaction_with_commitment(
                &Signature::from_str(signature.as_str()).unwrap(),
                CommitmentConfig::finalized(),
            )
            .map_err(|e| VtError::ClientError(e.to_string()))?;

        let signature = Signature::from_str(signature.as_str()).map_err(|e| {
            VtError::ConversionError(format!("Failed to convert signature to string: {}", e))
        })?;

        Ok(signature)
    }

    pub async fn async_sign_and_send(self, client: &AsyncRpcClient) -> Result<Signature, VtError> {
        let serialized_versioned_tx =
            bincode::serialize(&self).map_err(|e| VtError::SerializationError(e.to_string()))?;

        let serialized_encoded = base64::encode(serialized_versioned_tx);
        let rpc_config = RpcSendTransactionConfig {
            skip_preflight: false,
            preflight_commitment: Some(CommitmentLevel::Processed),
            encoding: Some(UiTransactionEncoding::Base64),
            ..RpcSendTransactionConfig::default()
        };

        // Have to do some manual RPC calls here because the v1.10 RPC client doesn't support
        // sending versioned transactions.

        let signature = client
            .send::<String>(
                RpcRequest::SendTransaction,
                json!([serialized_encoded, rpc_config]),
            )
            .await
            .map_err(|e| VtError::ClientError(e.to_string()))?;

        client
            .confirm_transaction_with_commitment(
                &Signature::from_str(signature.as_str()).unwrap(),
                CommitmentConfig::finalized(),
            )
            .await
            .map_err(|e| VtError::ClientError(e.to_string()))?;

        let signature = Signature::from_str(signature.as_str()).map_err(|e| {
            VtError::ConversionError(format!("Failed to convert signature to string: {}", e))
        })?;

        Ok(signature)
    }
}


