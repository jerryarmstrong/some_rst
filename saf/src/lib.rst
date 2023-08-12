saf/src/lib.rs
==============

Last edited: 2022-11-28 20:53:26

Contents:

.. code-block:: rs

    mod account_constraints;
mod account_info;
mod constraints;
mod error;
mod plan;
mod utils;  

pub use account_constraints::*;
use account_info::AccountInfoContext;
pub use constraints::*;
pub use error::*;
pub use plan::*;
use solana_program::{account_info::AccountInfo, pubkey::Pubkey};
use solana_program::{example_mocks::solana_sdk::transaction::Transaction, instruction::Instruction};

pub enum AccountIndex{
    Index(u8),
    None
}

pub trait ToInstruction: InstructionData + ToAccounts {
    type Variant;
    fn discriminator() -> &'static u16;

    fn to_instruction(variant: self::Variant) -> Instruction;
}

pub trait InstructionData: Sized {
    type Data;

    fn from_raw(data: &[u8]) -> Result<Self, AccountsError>;
    fn data(&self) -> Self::Data;
}

pub trait ToAccounts: Sized {
    type AccountPlan;
    // fn to_accounts_owned<'a>(accounts: &'a [AccountInfo]) -> Vec<AccountInfo>;

    // fn to_accounts_ref<'a>(accounts: &'a [AccountInfo]) -> Vec<&'a AccountInfo>;

    fn to_account_plan<'a>(&self, accounts: &'a [AccountInfo]) -> Self::AccountPlan;
}

pub struct Processor {}

impl Processor {
    pub fn entrypoint(
        program_id: &Pubkey,
        accounts: &[AccountInfo],
        instruction_data: &[u8],
        handlers: Vec<impl ToInstruction>,
    ) -> Result<(), AccountsError> {
        let ix = &instruction_data[0..2];
        let ix = u16::from_le_bytes([ix[0], ix[1]]);
        Ok(())
    }
}

#[cfg(test)]
mod tests {
    

    use solana_program::instruction::AccountMeta;

    use super::*;

    #[derive(Debug, Clone)]
    pub enum TokenStandard {
        Nft,
        FT,
        SFT,
    }

    pub struct Mint {
        owner: AccountMeta,
        metadata: AccountMeta,
        mint: AccountMeta,
        update_authority: AccountMeta,
        uri: String,
        name: String,
        token_standard: TokenStandard,
    }
    // #[derive(MsgPackData, Accounts)]  // #[derive(BorshData, Accounts)]
    pub enum MintArgs {
        V1 {
            owner: AccountIndex,
            metadata: AccountIndex,
            mint: AccountIndex,
            update_authority: AccountIndex,
            uri: String,
            name: String,
            token_standard: TokenStandard,
        },
    }

    pub enum MintArgsBuilder {
        V1 {
            owner: Pubkey,
            metadata: Pubkey,
            mint: Pubkey,
            update_authority: Pubkey,
            uri: String,
            name: String,
            token_standard: TokenStandard,
        },
    }

    pub struct MintV1Accounts<'a> {
        owner: &'a AccountInfo<'a>,
        metadata: &'a AccountInfo<'a>,
        mint: &'a AccountInfo<'a>,
        update_authority: &'a AccountInfo<'a>,
    }

    pub struct MintV1Data {
        uri: String,
        name: String,
        token_standard: TokenStandard,
    }

    impl ToInstruction for MintArgs::V1 {
        type Variant = MintArgs<'a>;
        fn discriminator() -> &'static u16 {
            &0x0001
        }

        fn to_instruction(&self) -> Instruction {
            let mut data = vec![];
            data.extend_from_slice(&Self::discriminator().to_le_bytes());
            data.extend_from_slice(&self.data());
            Instruction {
                program_id: Pubkey::default(),
                accounts: vec![


                ],
                data,
            }
        }

    }

    impl<'a> ToAccounts for MintArgs {
        type AccountPlan = MintV1Accounts<'a>;
       

        fn to_account_list(&self, accounts: &'a [AccountInfo]) -> Self::AccountPlan {
            let ctx = AccountInfoContext::new(accounts);
            MintV1Accounts {
                owner: ctx.get_account(self.owner),
                metadata: ctx.get_account(self.metadata),
                mint: ctx.get_account(self.mint),
                update_authority: ctx.get_account(self.update_authority),
            }
        }

        fn to_account_plan(&self, accounts: &'a [AccountInfo]) -> Self::AccountPlan {
            match self {
                MintArgs::V1 {
                    owner,
                    metadata,
                    mint,
                    update_authority,
                    uri,
                    name,
                    token_standard,
                } => {
                    let owner = &accounts.get(owner.0 as usize)
                    .ok_or(AccountsError::RequiredAccountMissing).unwrap();
                    


                    MintV1Accounts {
                    owner: owner,
                    metadata: *metadata,
                    mint: *mint,
                    update_authority: *update_authority,
                }
            }
            }
        }
    }

    impl InstructionData for MintArgs {
        type Data = MintV1Data;

        fn data(&self) -> Self::Data {
            match self {
                MintArgs::V1 {
                    uri,
                    name,
                    token_standard,
                    ..
                } => MintV1Data {
                    uri: uri.clone(),
                    name: name.clone(),
                    token_standard: token_standard.clone(),
                },
            }
        }

        fn from_raw(data: &[u8]) -> Result<Self, AccountsError> {
            let mut data = data;
            let owner = AccountIndex(0);
            let metadata = AccountIndex(1);
            let mint = AccountIndex(2);
            let update_authority = AccountIndex(3);

            let uri = String::from_utf8(data[4..].to_vec()).unwrap();
            let name = String::from_utf8(data[4..].to_vec()).unwrap();
            let token_standard = TokenStandard::Nft;

            Ok(Self::V1 {
                owner,
                metadata,
                mint,
                update_authority,
                uri,
                name,
                token_standard,
            })
        }
    }


    #[tokio::test]
    fn test() {
    
        let ins = 
        let tx = Transaction::new_with_payer(
            &[],
            Some(&Pubkey::new_unique()),
        );
    }
}


