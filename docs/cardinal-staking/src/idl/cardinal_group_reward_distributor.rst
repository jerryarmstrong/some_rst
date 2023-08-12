src/idl/cardinal_group_reward_distributor.ts
============================================

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: ts

    export type CardinalGroupRewardDistributor = {
  version: "2.2.1";
  name: "cardinal_group_reward_distributor";
  instructions: [
    {
      name: "initGroupRewardDistributor";
      accounts: [
        {
          name: "groupRewardDistributor";
          isMut: true;
          isSigner: false;
        },
        {
          name: "rewardMint";
          isMut: true;
          isSigner: false;
        },
        {
          name: "authority";
          isMut: true;
          isSigner: true;
        },
        {
          name: "payer";
          isMut: true;
          isSigner: true;
        },
        {
          name: "tokenProgram";
          isMut: false;
          isSigner: false;
        },
        {
          name: "systemProgram";
          isMut: false;
          isSigner: false;
        }
      ];
      args: [
        {
          name: "ix";
          type: {
            defined: "InitGroupRewardDistributorIx";
          };
        }
      ];
    },
    {
      name: "initGroupRewardEntry";
      accounts: [
        {
          name: "groupRewardEntry";
          isMut: true;
          isSigner: false;
        },
        {
          name: "groupRewardCounter";
          isMut: true;
          isSigner: false;
        },
        {
          name: "groupEntry";
          isMut: true;
          isSigner: false;
        },
        {
          name: "groupRewardDistributor";
          isMut: true;
          isSigner: false;
        },
        {
          name: "authority";
          isMut: true;
          isSigner: true;
        },
        {
          name: "systemProgram";
          isMut: false;
          isSigner: false;
        }
      ];
      args: [];
    },
    {
      name: "claimGroupRewards";
      accounts: [
        {
          name: "groupEntry";
          isMut: true;
          isSigner: false;
        },
        {
          name: "groupRewardCounter";
          isMut: true;
          isSigner: false;
        },
        {
          name: "groupRewardEntry";
          isMut: true;
          isSigner: false;
        },
        {
          name: "groupRewardDistributor";
          isMut: true;
          isSigner: false;
        },
        {
          name: "rewardMint";
          isMut: true;
          isSigner: false;
        },
        {
          name: "userRewardMintTokenAccount";
          isMut: true;
          isSigner: false;
        },
        {
          name: "rewardManager";
          isMut: true;
          isSigner: false;
        },
        {
          name: "authority";
          isMut: true;
          isSigner: true;
        },
        {
          name: "tokenProgram";
          isMut: false;
          isSigner: false;
        },
        {
          name: "systemProgram";
          isMut: false;
          isSigner: false;
        }
      ];
      args: [];
    },
    {
      name: "updateGroupRewardEntry";
      accounts: [
        {
          name: "groupRewardEntry";
          isMut: true;
          isSigner: false;
        },
        {
          name: "groupRewardDistributor";
          isMut: false;
          isSigner: false;
        },
        {
          name: "authority";
          isMut: false;
          isSigner: true;
        }
      ];
      args: [
        {
          name: "ix";
          type: {
            defined: "UpdateGroupRewardEntryIx";
          };
        }
      ];
    },
    {
      name: "closeGroupRewardDistributor";
      accounts: [
        {
          name: "groupRewardDistributor";
          isMut: true;
          isSigner: false;
        },
        {
          name: "rewardMint";
          isMut: true;
          isSigner: false;
        },
        {
          name: "authority";
          isMut: true;
          isSigner: true;
        },
        {
          name: "tokenProgram";
          isMut: false;
          isSigner: false;
        }
      ];
      args: [];
    },
    {
      name: "closeGroupRewardEntry";
      accounts: [
        {
          name: "groupRewardEntry";
          isMut: true;
          isSigner: false;
        },
        {
          name: "groupRewardCounter";
          isMut: true;
          isSigner: false;
        },
        {
          name: "groupRewardDistributor";
          isMut: true;
          isSigner: false;
        },
        {
          name: "groupEntry";
          isMut: true;
          isSigner: false;
        },
        {
          name: "authority";
          isMut: true;
          isSigner: true;
        }
      ];
      args: [];
    },
    {
      name: "updateGroupRewardDistributor";
      accounts: [
        {
          name: "groupRewardDistributor";
          isMut: true;
          isSigner: false;
        },
        {
          name: "authority";
          isMut: false;
          isSigner: true;
        },
        {
          name: "systemProgram";
          isMut: false;
          isSigner: false;
        }
      ];
      args: [
        {
          name: "ix";
          type: {
            defined: "UpdateGroupRewardDistributorIx";
          };
        }
      ];
    },
    {
      name: "reclaimGroupFunds";
      accounts: [
        {
          name: "groupRewardDistributor";
          isMut: true;
          isSigner: false;
        },
        {
          name: "groupRewardDistributorTokenAccount";
          isMut: true;
          isSigner: false;
        },
        {
          name: "authorityTokenAccount";
          isMut: true;
          isSigner: false;
        },
        {
          name: "authority";
          isMut: true;
          isSigner: true;
        },
        {
          name: "tokenProgram";
          isMut: false;
          isSigner: false;
        }
      ];
      args: [
        {
          name: "amount";
          type: "u64";
        }
      ];
    },
    {
      name: "initGroupRewardCounter";
      accounts: [
        {
          name: "groupRewardCounter";
          isMut: true;
          isSigner: false;
        },
        {
          name: "groupRewardDistributor";
          isMut: true;
          isSigner: false;
        },
        {
          name: "authority";
          isMut: true;
          isSigner: true;
        },
        {
          name: "systemProgram";
          isMut: false;
          isSigner: false;
        }
      ];
      args: [];
    },
    {
      name: "closeGroupRewardCounter";
      accounts: [
        {
          name: "groupRewardCounter";
          isMut: true;
          isSigner: false;
        },
        {
          name: "groupRewardDistributor";
          isMut: true;
          isSigner: false;
        },
        {
          name: "authority";
          isMut: true;
          isSigner: true;
        }
      ];
      args: [];
    }
  ];
  accounts: [
    {
      name: "groupRewardCounter";
      type: {
        kind: "struct";
        fields: [
          {
            name: "bump";
            type: "u8";
          },
          {
            name: "groupRewardDistributor";
            type: "publicKey";
          },
          {
            name: "authority";
            type: "publicKey";
          },
          {
            name: "count";
            type: "u64";
          }
        ];
      };
    },
    {
      name: "groupRewardEntry";
      type: {
        kind: "struct";
        fields: [
          {
            name: "bump";
            type: "u8";
          },
          {
            name: "groupEntry";
            type: "publicKey";
          },
          {
            name: "groupRewardDistributor";
            type: "publicKey";
          },
          {
            name: "rewardSecondsReceived";
            type: "u128";
          },
          {
            name: "multiplier";
            type: "u64";
          }
        ];
      };
    },
    {
      name: "groupRewardDistributor";
      type: {
        kind: "struct";
        fields: [
          {
            name: "bump";
            type: "u8";
          },
          {
            name: "id";
            type: "publicKey";
          },
          {
            name: "authorizedPools";
            type: {
              vec: "publicKey";
            };
          },
          {
            name: "rewardKind";
            type: {
              defined: "GroupRewardDistributorKind";
            };
          },
          {
            name: "metadataKind";
            type: {
              defined: "GroupRewardDistributorMetadataKind";
            };
          },
          {
            name: "poolKind";
            type: {
              defined: "GroupRewardDistributorPoolKind";
            };
          },
          {
            name: "authority";
            type: "publicKey";
          },
          {
            name: "rewardMint";
            type: "publicKey";
          },
          {
            name: "rewardAmount";
            type: "u64";
          },
          {
            name: "rewardDurationSeconds";
            type: "u128";
          },
          {
            name: "rewardsIssued";
            type: "u128";
          },
          {
            name: "baseAdder";
            type: "u64";
          },
          {
            name: "baseAdderDecimals";
            type: "u8";
          },
          {
            name: "baseMultiplier";
            type: "u64";
          },
          {
            name: "baseMultiplierDecimals";
            type: "u8";
          },
          {
            name: "multiplierDecimals";
            type: "u8";
          },
          {
            name: "minCooldownSeconds";
            type: "u32";
          },
          {
            name: "minStakeSeconds";
            type: "u32";
          },
          {
            name: "maxSupply";
            type: {
              option: "u64";
            };
          },
          {
            name: "groupCountMultiplier";
            type: {
              option: "u64";
            };
          },
          {
            name: "groupCountMultiplierDecimals";
            type: {
              option: "u8";
            };
          },
          {
            name: "minGroupSize";
            type: {
              option: "u8";
            };
          },
          {
            name: "maxRewardSecondsReceived";
            type: {
              option: "u128";
            };
          },
          {
            name: "authorizedCreators";
            type: {
              option: {
                vec: "publicKey";
              };
            };
          }
        ];
      };
    }
  ];
  types: [
    {
      name: "InitGroupRewardDistributorIx";
      type: {
        kind: "struct";
        fields: [
          {
            name: "id";
            type: "publicKey";
          },
          {
            name: "rewardAmount";
            type: "u64";
          },
          {
            name: "rewardDurationSeconds";
            type: "u128";
          },
          {
            name: "rewardKind";
            type: "u8";
          },
          {
            name: "metadataKind";
            type: "u8";
          },
          {
            name: "poolKind";
            type: "u8";
          },
          {
            name: "authorizedPools";
            type: {
              vec: "publicKey";
            };
          },
          {
            name: "authorizedCreators";
            type: {
              option: {
                vec: "publicKey";
              };
            };
          },
          {
            name: "supply";
            type: {
              option: "u64";
            };
          },
          {
            name: "baseAdder";
            type: {
              option: "u64";
            };
          },
          {
            name: "baseAdderDecimals";
            type: {
              option: "u8";
            };
          },
          {
            name: "baseMultiplier";
            type: {
              option: "u64";
            };
          },
          {
            name: "baseMultiplierDecimals";
            type: {
              option: "u8";
            };
          },
          {
            name: "multiplierDecimals";
            type: {
              option: "u8";
            };
          },
          {
            name: "maxSupply";
            type: {
              option: "u64";
            };
          },
          {
            name: "minCooldownSeconds";
            type: {
              option: "u32";
            };
          },
          {
            name: "minStakeSeconds";
            type: {
              option: "u32";
            };
          },
          {
            name: "groupCountMultiplier";
            type: {
              option: "u64";
            };
          },
          {
            name: "groupCountMultiplierDecimals";
            type: {
              option: "u8";
            };
          },
          {
            name: "minGroupSize";
            type: {
              option: "u8";
            };
          },
          {
            name: "maxRewardSecondsReceived";
            type: {
              option: "u128";
            };
          }
        ];
      };
    },
    {
      name: "UpdateGroupRewardDistributorIx";
      type: {
        kind: "struct";
        fields: [
          {
            name: "rewardAmount";
            type: "u64";
          },
          {
            name: "rewardDurationSeconds";
            type: "u128";
          },
          {
            name: "metadataKind";
            type: "u8";
          },
          {
            name: "poolKind";
            type: "u8";
          },
          {
            name: "authorizedPools";
            type: {
              vec: "publicKey";
            };
          },
          {
            name: "authorizedCreators";
            type: {
              option: {
                vec: "publicKey";
              };
            };
          },
          {
            name: "baseAdder";
            type: {
              option: "u64";
            };
          },
          {
            name: "baseAdderDecimals";
            type: {
              option: "u8";
            };
          },
          {
            name: "baseMultiplier";
            type: {
              option: "u64";
            };
          },
          {
            name: "baseMultiplierDecimals";
            type: {
              option: "u8";
            };
          },
          {
            name: "multiplierDecimals";
            type: {
              option: "u8";
            };
          },
          {
            name: "maxSupply";
            type: {
              option: "u64";
            };
          },
          {
            name: "minCooldownSeconds";
            type: {
              option: "u32";
            };
          },
          {
            name: "minStakeSeconds";
            type: {
              option: "u32";
            };
          },
          {
            name: "groupCountMultiplier";
            type: {
              option: "u64";
            };
          },
          {
            name: "groupCountMultiplierDecimals";
            type: {
              option: "u8";
            };
          },
          {
            name: "minGroupSize";
            type: {
              option: "u8";
            };
          },
          {
            name: "maxRewardSecondsReceived";
            type: {
              option: "u128";
            };
          }
        ];
      };
    },
    {
      name: "UpdateGroupRewardEntryIx";
      type: {
        kind: "struct";
        fields: [
          {
            name: "multiplier";
            type: "u64";
          }
        ];
      };
    },
    {
      name: "GroupRewardDistributorKind";
      type: {
        kind: "enum";
        variants: [
          {
            name: "Mint";
          },
          {
            name: "Treasury";
          }
        ];
      };
    },
    {
      name: "GroupRewardDistributorMetadataKind";
      type: {
        kind: "enum";
        variants: [
          {
            name: "NoRestriction";
          },
          {
            name: "UniqueNames";
          },
          {
            name: "UniqueSymbols";
          }
        ];
      };
    },
    {
      name: "GroupRewardDistributorPoolKind";
      type: {
        kind: "enum";
        variants: [
          {
            name: "NoRestriction";
          },
          {
            name: "AllFromSinglePool";
          },
          {
            name: "EachFromSeparatePool";
          }
        ];
      };
    }
  ];
  errors: [
    {
      code: 6000;
      name: "InvalidRewardMint";
      msg: "Invalid reward mint";
    },
    {
      code: 6001;
      name: "InvalidUserRewardMintTokenAccount";
      msg: "Invalid user reward mint token account";
    },
    {
      code: 6002;
      name: "InvalidRewardDistributor";
      msg: "Invalid reward distributor";
    },
    {
      code: 6003;
      name: "InvalidRewardDistributorKind";
      msg: "Invalid reward distributor kind";
    },
    {
      code: 6004;
      name: "SupplyRequired";
      msg: "Initial supply required for kind treasury";
    },
    {
      code: 6005;
      name: "InvalidAuthority";
      msg: "Invalid authority";
    },
    {
      code: 6006;
      name: "InvalidStakeEntry";
      msg: "Invalid stake entry";
    },
    {
      code: 6007;
      name: "InvalidRewardDistributorTokenAccount";
      msg: "Invalid reward distributor token account";
    },
    {
      code: 6008;
      name: "InvalidAuthorityTokenAccount";
      msg: "Invalid authority token account";
    },
    {
      code: 6009;
      name: "InvalidGroupSize";
      msg: "Invalid group size";
    },
    {
      code: 6010;
      name: "InvalidPool";
      msg: "Invalid pool";
    },
    {
      code: 6011;
      name: "InvalidOriginalMint";
      msg: "Original mint is invalid";
    },
    {
      code: 6012;
      name: "InvalidMintMetadata";
      msg: "Invalid mint metadata";
    },
    {
      code: 6013;
      name: "InvalidMintMetadataOwner";
      msg: "Mint metadata is owned by the incorrect program";
    },
    {
      code: 6014;
      name: "InvalidRewardEntry";
      msg: "Invalid reward entry";
    },
    {
      code: 6015;
      name: "InvalidGroupSeconds";
      msg: "Invalid group seconds";
    },
    {
      code: 6016;
      name: "InvalidCooldownSeconds";
      msg: "Invalid cooldown seconds";
    }
  ];
};

export const IDL: CardinalGroupRewardDistributor = {
  version: "2.2.1",
  name: "cardinal_group_reward_distributor",
  instructions: [
    {
      name: "initGroupRewardDistributor",
      accounts: [
        {
          name: "groupRewardDistributor",
          isMut: true,
          isSigner: false,
        },
        {
          name: "rewardMint",
          isMut: true,
          isSigner: false,
        },
        {
          name: "authority",
          isMut: true,
          isSigner: true,
        },
        {
          name: "payer",
          isMut: true,
          isSigner: true,
        },
        {
          name: "tokenProgram",
          isMut: false,
          isSigner: false,
        },
        {
          name: "systemProgram",
          isMut: false,
          isSigner: false,
        },
      ],
      args: [
        {
          name: "ix",
          type: {
            defined: "InitGroupRewardDistributorIx",
          },
        },
      ],
    },
    {
      name: "initGroupRewardEntry",
      accounts: [
        {
          name: "groupRewardEntry",
          isMut: true,
          isSigner: false,
        },
        {
          name: "groupRewardCounter",
          isMut: true,
          isSigner: false,
        },
        {
          name: "groupEntry",
          isMut: true,
          isSigner: false,
        },
        {
          name: "groupRewardDistributor",
          isMut: true,
          isSigner: false,
        },
        {
          name: "authority",
          isMut: true,
          isSigner: true,
        },
        {
          name: "systemProgram",
          isMut: false,
          isSigner: false,
        },
      ],
      args: [],
    },
    {
      name: "claimGroupRewards",
      accounts: [
        {
          name: "groupEntry",
          isMut: true,
          isSigner: false,
        },
        {
          name: "groupRewardCounter",
          isMut: true,
          isSigner: false,
        },
        {
          name: "groupRewardEntry",
          isMut: true,
          isSigner: false,
        },
        {
          name: "groupRewardDistributor",
          isMut: true,
          isSigner: false,
        },
        {
          name: "rewardMint",
          isMut: true,
          isSigner: false,
        },
        {
          name: "userRewardMintTokenAccount",
          isMut: true,
          isSigner: false,
        },
        {
          name: "rewardManager",
          isMut: true,
          isSigner: false,
        },
        {
          name: "authority",
          isMut: true,
          isSigner: true,
        },
        {
          name: "tokenProgram",
          isMut: false,
          isSigner: false,
        },
        {
          name: "systemProgram",
          isMut: false,
          isSigner: false,
        },
      ],
      args: [],
    },
    {
      name: "updateGroupRewardEntry",
      accounts: [
        {
          name: "groupRewardEntry",
          isMut: true,
          isSigner: false,
        },
        {
          name: "groupRewardDistributor",
          isMut: false,
          isSigner: false,
        },
        {
          name: "authority",
          isMut: false,
          isSigner: true,
        },
      ],
      args: [
        {
          name: "ix",
          type: {
            defined: "UpdateGroupRewardEntryIx",
          },
        },
      ],
    },
    {
      name: "closeGroupRewardDistributor",
      accounts: [
        {
          name: "groupRewardDistributor",
          isMut: true,
          isSigner: false,
        },
        {
          name: "rewardMint",
          isMut: true,
          isSigner: false,
        },
        {
          name: "authority",
          isMut: true,
          isSigner: true,
        },
        {
          name: "tokenProgram",
          isMut: false,
          isSigner: false,
        },
      ],
      args: [],
    },
    {
      name: "closeGroupRewardEntry",
      accounts: [
        {
          name: "groupRewardEntry",
          isMut: true,
          isSigner: false,
        },
        {
          name: "groupRewardCounter",
          isMut: true,
          isSigner: false,
        },
        {
          name: "groupRewardDistributor",
          isMut: true,
          isSigner: false,
        },
        {
          name: "groupEntry",
          isMut: true,
          isSigner: false,
        },
        {
          name: "authority",
          isMut: true,
          isSigner: true,
        },
      ],
      args: [],
    },
    {
      name: "updateGroupRewardDistributor",
      accounts: [
        {
          name: "groupRewardDistributor",
          isMut: true,
          isSigner: false,
        },
        {
          name: "authority",
          isMut: false,
          isSigner: true,
        },
        {
          name: "systemProgram",
          isMut: false,
          isSigner: false,
        },
      ],
      args: [
        {
          name: "ix",
          type: {
            defined: "UpdateGroupRewardDistributorIx",
          },
        },
      ],
    },
    {
      name: "reclaimGroupFunds",
      accounts: [
        {
          name: "groupRewardDistributor",
          isMut: true,
          isSigner: false,
        },
        {
          name: "groupRewardDistributorTokenAccount",
          isMut: true,
          isSigner: false,
        },
        {
          name: "authorityTokenAccount",
          isMut: true,
          isSigner: false,
        },
        {
          name: "authority",
          isMut: true,
          isSigner: true,
        },
        {
          name: "tokenProgram",
          isMut: false,
          isSigner: false,
        },
      ],
      args: [
        {
          name: "amount",
          type: "u64",
        },
      ],
    },
    {
      name: "initGroupRewardCounter",
      accounts: [
        {
          name: "groupRewardCounter",
          isMut: true,
          isSigner: false,
        },
        {
          name: "groupRewardDistributor",
          isMut: true,
          isSigner: false,
        },
        {
          name: "authority",
          isMut: true,
          isSigner: true,
        },
        {
          name: "systemProgram",
          isMut: false,
          isSigner: false,
        },
      ],
      args: [],
    },
    {
      name: "closeGroupRewardCounter",
      accounts: [
        {
          name: "groupRewardCounter",
          isMut: true,
          isSigner: false,
        },
        {
          name: "groupRewardDistributor",
          isMut: true,
          isSigner: false,
        },
        {
          name: "authority",
          isMut: true,
          isSigner: true,
        },
      ],
      args: [],
    },
  ],
  accounts: [
    {
      name: "groupRewardCounter",
      type: {
        kind: "struct",
        fields: [
          {
            name: "bump",
            type: "u8",
          },
          {
            name: "groupRewardDistributor",
            type: "publicKey",
          },
          {
            name: "authority",
            type: "publicKey",
          },
          {
            name: "count",
            type: "u64",
          },
        ],
      },
    },
    {
      name: "groupRewardEntry",
      type: {
        kind: "struct",
        fields: [
          {
            name: "bump",
            type: "u8",
          },
          {
            name: "groupEntry",
            type: "publicKey",
          },
          {
            name: "groupRewardDistributor",
            type: "publicKey",
          },
          {
            name: "rewardSecondsReceived",
            type: "u128",
          },
          {
            name: "multiplier",
            type: "u64",
          },
        ],
      },
    },
    {
      name: "groupRewardDistributor",
      type: {
        kind: "struct",
        fields: [
          {
            name: "bump",
            type: "u8",
          },
          {
            name: "id",
            type: "publicKey",
          },
          {
            name: "authorizedPools",
            type: {
              vec: "publicKey",
            },
          },
          {
            name: "rewardKind",
            type: {
              defined: "GroupRewardDistributorKind",
            },
          },
          {
            name: "metadataKind",
            type: {
              defined: "GroupRewardDistributorMetadataKind",
            },
          },
          {
            name: "poolKind",
            type: {
              defined: "GroupRewardDistributorPoolKind",
            },
          },
          {
            name: "authority",
            type: "publicKey",
          },
          {
            name: "rewardMint",
            type: "publicKey",
          },
          {
            name: "rewardAmount",
            type: "u64",
          },
          {
            name: "rewardDurationSeconds",
            type: "u128",
          },
          {
            name: "rewardsIssued",
            type: "u128",
          },
          {
            name: "baseAdder",
            type: "u64",
          },
          {
            name: "baseAdderDecimals",
            type: "u8",
          },
          {
            name: "baseMultiplier",
            type: "u64",
          },
          {
            name: "baseMultiplierDecimals",
            type: "u8",
          },
          {
            name: "multiplierDecimals",
            type: "u8",
          },
          {
            name: "minCooldownSeconds",
            type: "u32",
          },
          {
            name: "minStakeSeconds",
            type: "u32",
          },
          {
            name: "maxSupply",
            type: {
              option: "u64",
            },
          },
          {
            name: "groupCountMultiplier",
            type: {
              option: "u64",
            },
          },
          {
            name: "groupCountMultiplierDecimals",
            type: {
              option: "u8",
            },
          },
          {
            name: "minGroupSize",
            type: {
              option: "u8",
            },
          },
          {
            name: "maxRewardSecondsReceived",
            type: {
              option: "u128",
            },
          },
          {
            name: "authorizedCreators",
            type: {
              option: {
                vec: "publicKey",
              },
            },
          },
        ],
      },
    },
  ],
  types: [
    {
      name: "InitGroupRewardDistributorIx",
      type: {
        kind: "struct",
        fields: [
          {
            name: "id",
            type: "publicKey",
          },
          {
            name: "rewardAmount",
            type: "u64",
          },
          {
            name: "rewardDurationSeconds",
            type: "u128",
          },
          {
            name: "rewardKind",
            type: "u8",
          },
          {
            name: "metadataKind",
            type: "u8",
          },
          {
            name: "poolKind",
            type: "u8",
          },
          {
            name: "authorizedPools",
            type: {
              vec: "publicKey",
            },
          },
          {
            name: "authorizedCreators",
            type: {
              option: {
                vec: "publicKey",
              },
            },
          },
          {
            name: "supply",
            type: {
              option: "u64",
            },
          },
          {
            name: "baseAdder",
            type: {
              option: "u64",
            },
          },
          {
            name: "baseAdderDecimals",
            type: {
              option: "u8",
            },
          },
          {
            name: "baseMultiplier",
            type: {
              option: "u64",
            },
          },
          {
            name: "baseMultiplierDecimals",
            type: {
              option: "u8",
            },
          },
          {
            name: "multiplierDecimals",
            type: {
              option: "u8",
            },
          },
          {
            name: "maxSupply",
            type: {
              option: "u64",
            },
          },
          {
            name: "minCooldownSeconds",
            type: {
              option: "u32",
            },
          },
          {
            name: "minStakeSeconds",
            type: {
              option: "u32",
            },
          },
          {
            name: "groupCountMultiplier",
            type: {
              option: "u64",
            },
          },
          {
            name: "groupCountMultiplierDecimals",
            type: {
              option: "u8",
            },
          },
          {
            name: "minGroupSize",
            type: {
              option: "u8",
            },
          },
          {
            name: "maxRewardSecondsReceived",
            type: {
              option: "u128",
            },
          },
        ],
      },
    },
    {
      name: "UpdateGroupRewardDistributorIx",
      type: {
        kind: "struct",
        fields: [
          {
            name: "rewardAmount",
            type: "u64",
          },
          {
            name: "rewardDurationSeconds",
            type: "u128",
          },
          {
            name: "metadataKind",
            type: "u8",
          },
          {
            name: "poolKind",
            type: "u8",
          },
          {
            name: "authorizedPools",
            type: {
              vec: "publicKey",
            },
          },
          {
            name: "authorizedCreators",
            type: {
              option: {
                vec: "publicKey",
              },
            },
          },
          {
            name: "baseAdder",
            type: {
              option: "u64",
            },
          },
          {
            name: "baseAdderDecimals",
            type: {
              option: "u8",
            },
          },
          {
            name: "baseMultiplier",
            type: {
              option: "u64",
            },
          },
          {
            name: "baseMultiplierDecimals",
            type: {
              option: "u8",
            },
          },
          {
            name: "multiplierDecimals",
            type: {
              option: "u8",
            },
          },
          {
            name: "maxSupply",
            type: {
              option: "u64",
            },
          },
          {
            name: "minCooldownSeconds",
            type: {
              option: "u32",
            },
          },
          {
            name: "minStakeSeconds",
            type: {
              option: "u32",
            },
          },
          {
            name: "groupCountMultiplier",
            type: {
              option: "u64",
            },
          },
          {
            name: "groupCountMultiplierDecimals",
            type: {
              option: "u8",
            },
          },
          {
            name: "minGroupSize",
            type: {
              option: "u8",
            },
          },
          {
            name: "maxRewardSecondsReceived",
            type: {
              option: "u128",
            },
          },
        ],
      },
    },
    {
      name: "UpdateGroupRewardEntryIx",
      type: {
        kind: "struct",
        fields: [
          {
            name: "multiplier",
            type: "u64",
          },
        ],
      },
    },
    {
      name: "GroupRewardDistributorKind",
      type: {
        kind: "enum",
        variants: [
          {
            name: "Mint",
          },
          {
            name: "Treasury",
          },
        ],
      },
    },
    {
      name: "GroupRewardDistributorMetadataKind",
      type: {
        kind: "enum",
        variants: [
          {
            name: "NoRestriction",
          },
          {
            name: "UniqueNames",
          },
          {
            name: "UniqueSymbols",
          },
        ],
      },
    },
    {
      name: "GroupRewardDistributorPoolKind",
      type: {
        kind: "enum",
        variants: [
          {
            name: "NoRestriction",
          },
          {
            name: "AllFromSinglePool",
          },
          {
            name: "EachFromSeparatePool",
          },
        ],
      },
    },
  ],
  errors: [
    {
      code: 6000,
      name: "InvalidRewardMint",
      msg: "Invalid reward mint",
    },
    {
      code: 6001,
      name: "InvalidUserRewardMintTokenAccount",
      msg: "Invalid user reward mint token account",
    },
    {
      code: 6002,
      name: "InvalidRewardDistributor",
      msg: "Invalid reward distributor",
    },
    {
      code: 6003,
      name: "InvalidRewardDistributorKind",
      msg: "Invalid reward distributor kind",
    },
    {
      code: 6004,
      name: "SupplyRequired",
      msg: "Initial supply required for kind treasury",
    },
    {
      code: 6005,
      name: "InvalidAuthority",
      msg: "Invalid authority",
    },
    {
      code: 6006,
      name: "InvalidStakeEntry",
      msg: "Invalid stake entry",
    },
    {
      code: 6007,
      name: "InvalidRewardDistributorTokenAccount",
      msg: "Invalid reward distributor token account",
    },
    {
      code: 6008,
      name: "InvalidAuthorityTokenAccount",
      msg: "Invalid authority token account",
    },
    {
      code: 6009,
      name: "InvalidGroupSize",
      msg: "Invalid group size",
    },
    {
      code: 6010,
      name: "InvalidPool",
      msg: "Invalid pool",
    },
    {
      code: 6011,
      name: "InvalidOriginalMint",
      msg: "Original mint is invalid",
    },
    {
      code: 6012,
      name: "InvalidMintMetadata",
      msg: "Invalid mint metadata",
    },
    {
      code: 6013,
      name: "InvalidMintMetadataOwner",
      msg: "Mint metadata is owned by the incorrect program",
    },
    {
      code: 6014,
      name: "InvalidRewardEntry",
      msg: "Invalid reward entry",
    },
    {
      code: 6015,
      name: "InvalidGroupSeconds",
      msg: "Invalid group seconds",
    },
    {
      code: 6016,
      name: "InvalidCooldownSeconds",
      msg: "Invalid cooldown seconds",
    },
  ],
};


