examples/eggs/tests/utils/egg.rs
================================

Last edited: 2021-12-14 12:31:39

Contents:

.. code-block:: rs

    use super::{get_account, oracle::TestOracle};
use eggs::{id, instruction, state::Egg};
use solana_program::{program_pack::Pack, system_instruction};
use solana_program_test::ProgramTestContext;
use solana_sdk::{
    signature::{Keypair, Signer},
    transaction::Transaction,
    transport,
};

#[derive(Debug)]
pub struct TestEgg {
    pub keypair: Keypair,
}

impl TestEgg {
    pub fn new() -> Self {
        Self {
            keypair: Keypair::new(),
        }
    }

    pub async fn get_data(&self, context: &mut ProgramTestContext) -> Egg {
        let account = get_account(context, &self.keypair.pubkey()).await;
        Egg::unpack_unchecked(&account.data).unwrap()
    }

    pub async fn create(
        &self,
        context: &mut ProgramTestContext,
        oracle: &TestOracle,
    ) -> transport::Result<()> {
        let rent = context.banks_client.get_rent().await.unwrap();
        let tx = Transaction::new_signed_with_payer(
            &[
                system_instruction::create_account(
                    &context.payer.pubkey(),
                    &self.keypair.pubkey(),
                    rent.minimum_balance(Egg::LEN),
                    Egg::LEN as u64,
                    &id(),
                ),
                instruction::create_egg(&id(), &self.keypair.pubkey(), &oracle.pubkey),
            ],
            Some(&context.payer.pubkey()),
            &[&context.payer, &self.keypair],
            context.last_blockhash,
        );

        context.banks_client.process_transaction(tx).await
    }
}


