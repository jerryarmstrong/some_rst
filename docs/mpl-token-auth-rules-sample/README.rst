README.md
=========

Last edited: 2023-02-04 18:21:00

Contents:

.. code-block:: md

    # Metaplex SAMPLE RULESET
## NOT FINAL - The Final sample ruleset used for migration will be posted here as it gets updated, this currently contains test programs.

```json

{
   "libVersion": 1,
   "owner": [235,20,253,58,199,209,15,51,245,122,149,194,195,52,8,222,215,87,78,148,98,211,203,96,175,31,134,25,32,5,112,248],
   "ruleSetName": "Metaplex Royalty RuleSet Dev",
   "operations": {
      "Delegate:Staking": {
         "All": {
            "rules": [
               {
                  "Amount": {
                     "amount": 1,
                     "operator": "Eq",
                     "field": "Amount"
                  }
               },
               {
                  "ProgramOwnedList": {
                     "programs": [
                        [11,112,101,177,227,209,124,69,56,157,82,127,107,4,195,205,88,184,108,115,26,160,253,181,73,182,209,188,3,248,41,70],
                        [6,90,221,155,145,37,147,1,52,93,145,196,185,51,127,13,0,233,231,42,100,49,140,113,74,117,167,186,218,100,116,205]
                     ],
                     "field": "Delegate"
                  }
               }
            ]
         }
      },
      "Delegate:Utility": {
         "All": {
            "rules": [
               {
                  "Amount": {
                     "amount": 1,
                     "operator": "Eq",
                     "field": "Amount"
                  }
               },
               {
                  "ProgramOwnedList": {
                     "programs": [
                        [11,112,101,177,227,209,124,69,56,157,82,127,107,4,195,205,88,184,108,115,26,160,253,181,73,182,209,188,3,248,41,70],
                        [6,90,221,155,145,37,147,1,52,93,145,196,185,51,127,13,0,233,231,42,100,49,140,113,74,117,167,186,218,100,116,205]
                     ],
                     "field": "Delegate"
                  }
               }
            ]
         }
      },
      "Delegate:Authority": {
         "All": {
            "rules": [
               {
                  "Amount": {
                     "amount": 1,
                     "operator": "Eq",
                     "field": "Amount"
                  }
               },
               {
                  "ProgramOwnedList": {
                     "programs": [
                        [11,112,101,177,227,209,124,69,56,157,82,127,107,4,195,205,88,184,108,115,26,160,253,181,73,182,209,188,3,248,41,70],
                        [6,90,221,155,145,37,147,1,52,93,145,196,185,51,127,13,0,233,231,42,100,49,140,113,74,117,167,186,218,100,116,205]
                     ],
                     "field": "Delegate"
                  }
               }
            ]
         }
      },
      "Transfer:WalletToWallet": {
         "All": {
            "rules": [
               {
                  "Amount": {
                     "amount": 1,
                     "operator": "Eq",
                     "field": "Amount"
                  }
               },
               {
                  "IsWallet": {
                     "field": "Source"
                  }
               },
               {
                  "IsWallet": {
                     "field": "Destination"
                  }
               }
            ]
         }
      },
      "Transfer:MigrationDelegate": {
         "All": {
            "rules": [
               {
                  "Amount": {
                     "amount": 1,
                     "operator": "Eq",
                     "field": "Amount"
                  }
               },
               {
                  "Any": {
                     "rules": [
                        {
                           "ProgramOwnedList": {
                              "programs": [
                                [11,112,101,177,227,209,124,69,56,157,82,127,107,4,195,205,88,184,108,115,26,160,253,181,73,182,209,188,3,248,41,70],
                                [6,90,221,155,145,37,147,1,52,93,145,196,185,51,127,13,0,233,231,42,100,49,140,113,74,117,167,186,218,100,116,205]
                              ],
                              "field": "Source"
                           }
                        },
                        {
                           "ProgramOwnedList": {
                              "programs": [
                                [11,112,101,177,227,209,124,69,56,157,82,127,107,4,195,205,88,184,108,115,26,160,253,181,73,182,209,188,3,248,41,70],
                                [6,90,221,155,145,37,147,1,52,93,145,196,185,51,127,13,0,233,231,42,100,49,140,113,74,117,167,186,218,100,116,205]
                              ],
                              "field": "Destination"
                           }
                        },
                        {
                           "ProgramOwnedList": {
                              "programs": [
                                [11,112,101,177,227,209,124,69,56,157,82,127,107,4,195,205,88,184,108,115,26,160,253,181,73,182,209,188,3,248,41,70],
                                [6,90,221,155,145,37,147,1,52,93,145,196,185,51,127,13,0,233,231,42,100,49,140,113,74,117,167,186,218,100,116,205]
                              ],
                              "field": "Authority"
                           }
                        }
                     ]
                  }
               }
            ]
         }
      },
      "Transfer:TransferDelegate": {
         "All": {
            "rules": [
               {
                  "Amount": {
                     "amount": 1,
                     "operator": "Eq",
                     "field": "Amount"
                  }
               },
               {
                  "Any": {
                     "rules": [
                        {
                           "ProgramOwnedList": {
                              "programs": [
                                [11,112,101,177,227,209,124,69,56,157,82,127,107,4,195,205,88,184,108,115,26,160,253,181,73,182,209,188,3,248,41,70],
                                [6,90,221,155,145,37,147,1,52,93,145,196,185,51,127,13,0,233,231,42,100,49,140,113,74,117,167,186,218,100,116,205]
                              ],
                              "field": "Source"
                           }
                        },
                        {
                           "ProgramOwnedList": {
                              "programs": [
                                [11,112,101,177,227,209,124,69,56,157,82,127,107,4,195,205,88,184,108,115,26,160,253,181,73,182,209,188,3,248,41,70],
                                [6,90,221,155,145,37,147,1,52,93,145,196,185,51,127,13,0,233,231,42,100,49,140,113,74,117,167,186,218,100,116,205]
                              ],
                              "field": "Destination"
                           }
                        },
                        {
                           "ProgramOwnedList": {
                              "programs": [
                                [11,112,101,177,227,209,124,69,56,157,82,127,107,4,195,205,88,184,108,115,26,160,253,181,73,182,209,188,3,248,41,70],
                                [6,90,221,155,145,37,147,1,52,93,145,196,185,51,127,13,0,233,231,42,100,49,140,113,74,117,167,186,218,100,116,205]
                              ],
                              "field": "Authority"
                           }
                        }
                     ]
                  }
               }
            ]
         }
      },
      "Delegate:Use": {
         "All": {
            "rules": [
               {
                  "Amount": {
                     "amount": 1,
                     "operator": "Eq",
                     "field": "Amount"
                  }
               },
               {
                  "ProgramOwnedList": {
                     "programs": [
                        [11,112,101,177,227,209,124,69,56,157,82,127,107,4,195,205,88,184,108,115,26,160,253,181,73,182,209,188,3,248,41,70],
                        [6,90,221,155,145,37,147,1,52,93,145,196,185,51,127,13,0,233,231,42,100,49,140,113,74,117,167,186,218,100,116,205]
                     ],
                     "field": "Delegate"
                  }
               }
            ]
         }
      },
      "Delegate:Update": {
         "All": {
            "rules": [
               {
                  "Amount": {
                     "amount": 1,
                     "operator": "Eq",
                     "field": "Amount"
                  }
               },
               {
                  "ProgramOwnedList": {
                     "programs": [
                        [11,112,101,177,227,209,124,69,56,157,82,127,107,4,195,205,88,184,108,115,26,160,253,181,73,182,209,188,3,248,41,70],
                        [6,90,221,155,145,37,147,1,52,93,145,196,185,51,127,13,0,233,231,42,100,49,140,113,74,117,167,186,218,100,116,205]
                     ],
                     "field": "Delegate"
                  }
               }
            ]
         }
      },
      "Delegate:Collection": {
         "All": {
            "rules": [
               {
                  "Amount": {
                     "amount": 1,
                     "operator": "Eq",
                     "field": "Amount"
                  }
               },
               {
                  "ProgramOwnedList": {
                     "programs": [
                        [11,112,101,177,227,209,124,69,56,157,82,127,107,4,195,205,88,184,108,115,26,160,253,181,73,182,209,188,3,248,41,70],
                        [6,90,221,155,145,37,147,1,52,93,145,196,185,51,127,13,0,233,231,42,100,49,140,113,74,117,167,186,218,100,116,205]
                     ],
                     "field": "Delegate"
                  }
               }
            ]
         }
      },
      "Delegate:Sale": {
         "All": {
            "rules": [
               {
                  "Amount": {
                     "amount": 1,
                     "operator": "Eq",
                     "field": "Amount"
                  }
               },
               {
                  "ProgramOwnedList": {
                     "programs": [
                        [11,112,101,177,227,209,124,69,56,157,82,127,107,4,195,205,88,184,108,115,26,160,253,181,73,182,209,188,3,248,41,70],
                        [6,90,221,155,145,37,147,1,52,93,145,196,185,51,127,13,0,233,231,42,100,49,140,113,74,117,167,186,218,100,116,205]
                     ],
                     "field": "Delegate"
                  }
               }
            ]
         }
      },
      "Delegate:Transfer": {
         "All": {
            "rules": [
               {
                  "Amount": {
                     "amount": 1,
                     "operator": "Eq",
                     "field": "Amount"
                  }
               },
               {
                  "ProgramOwnedList": {
                     "programs": [
                        [11,112,101,177,227,209,124,69,56,157,82,127,107,4,195,205,88,184,108,115,26,160,253,181,73,182,209,188,3,248,41,70],
                        [6,90,221,155,145,37,147,1,52,93,145,196,185,51,127,13,0,233,231,42,100,49,140,113,74,117,167,186,218,100,116,205]
                     ],
                     "field": "Delegate"
                  }
               }
            ]
         }
      },
      "Transfer:Owner": {
         "All": {
            "rules": [
               {
                  "Amount": {
                     "amount": 1,
                     "operator": "Eq",
                     "field": "Amount"
                  }
               },
               {
                  "Any": {
                     "rules": [
                        {
                           "ProgramOwnedList": {
                              "programs": [
                                [11,112,101,177,227,209,124,69,56,157,82,127,107,4,195,205,88,184,108,115,26,160,253,181,73,182,209,188,3,248,41,70],
                                [6,90,221,155,145,37,147,1,52,93,145,196,185,51,127,13,0,233,231,42,100,49,140,113,74,117,167,186,218,100,116,205]
                              ],
                              "field": "Source"
                           }
                        },
                        {
                           "ProgramOwnedList": {
                              "programs": [
                                [11,112,101,177,227,209,124,69,56,157,82,127,107,4,195,205,88,184,108,115,26,160,253,181,73,182,209,188,3,248,41,70],
                                [6,90,221,155,145,37,147,1,52,93,145,196,185,51,127,13,0,233,231,42,100,49,140,113,74,117,167,186,218,100,116,205]
                              ],
                              "field": "Destination"
                           }
                        },
                        {
                           "ProgramOwnedList": {
                              "programs": [
                                [11,112,101,177,227,209,124,69,56,157,82,127,107,4,195,205,88,184,108,115,26,160,253,181,73,182,209,188,3,248,41,70],
                                [6,90,221,155,145,37,147,1,52,93,145,196,185,51,127,13,0,233,231,42,100,49,140,113,74,117,167,186,218,100,116,205]
                              ],
                              "field": "Authority"
                           }
                        }
                     ]
                  }
               }
            ]
         }
      },
      "Transfer:SaleDelegate": {
         "All": {
            "rules": [
               {
                  "Amount": {
                     "amount": 1,
                     "operator": "Eq",
                     "field": "Amount"
                  }
               },
               {
                  "Any": {
                     "rules": [
                        {
                           "ProgramOwnedList": {
                              "programs": [
                                [11,112,101,177,227,209,124,69,56,157,82,127,107,4,195,205,88,184,108,115,26,160,253,181,73,182,209,188,3,248,41,70],
                                [6,90,221,155,145,37,147,1,52,93,145,196,185,51,127,13,0,233,231,42,100,49,140,113,74,117,167,186,218,100,116,205]
                              ],
                              "field": "Source"
                           }
                        },
                        {
                           "ProgramOwnedList": {
                              "programs": [
                                [11,112,101,177,227,209,124,69,56,157,82,127,107,4,195,205,88,184,108,115,26,160,253,181,73,182,209,188,3,248,41,70],
                                [6,90,221,155,145,37,147,1,52,93,145,196,185,51,127,13,0,233,231,42,100,49,140,113,74,117,167,186,218,100,116,205]
                              ],
                              "field": "Destination"
                           }
                        },
                        {
                           "ProgramOwnedList": {
                              "programs": [
                                [11,112,101,177,227,209,124,69,56,157,82,127,107,4,195,205,88,184,108,115,26,160,253,181,73,182,209,188,3,248,41,70],
                                [6,90,221,155,145,37,147,1,52,93,145,196,185,51,127,13,0,233,231,42,100,49,140,113,74,117,167,186,218,100,116,205]
                              ],
                              "field": "Authority"
                           }
                        }
                     ]
                  }
               }
            ]
         }
      },
      "Delegate:LockedTransfer": {
         "All": {
            "rules": [
               {
                  "Amount": {
                     "amount": 1,
                     "operator": "Eq",
                     "field": "Amount"
                  }
               },
               {
                  "ProgramOwnedList": {
                     "programs": [
                        [11,112,101,177,227,209,124,69,56,157,82,127,107,4,195,205,88,184,108,115,26,160,253,181,73,182,209,188,3,248,41,70],
                        [6,90,221,155,145,37,147,1,52,93,145,196,185,51,127,13,0,233,231,42,100,49,140,113,74,117,167,186,218,100,116,205]
                     ],
                     "field": "Delegate"
                  }
               }
            ]
         }
      }
   }
}

```

This is the sample ruleset built on https://github.com/metaplex-foundation/token-authorization-rules.

## Tools
This repo contains a tool to use the sample ruleset. Below is an example of how to use it.

### Example
This will allow you to create the sample ruleset, if you would like to create your own ruleset you can use this as an example to tweak it.


Make sure you have rust installed, the easiest way to do this is to use rustup https://rustup.rs/.
Once you have rust installed you can run the below in this project directory.

NOTE this tool expects your keypari to be at "./keypair/devnet-test-rule-set-8.json"


```
$ cargo run
    Finished dev [unoptimized + debuginfo] target(s) in 0.13s
     Running `target/debug/mpl-token-auth-rules-example`
Metaplex Royalty RuleSet Dev: 8cZYUi7TSzSWoSGTnhxJdHtKyNskgRfeZQdtsqJkniMS
RuleSetV1 {
    lib_version: 1,
    owner: GydBYBTA4HbvjgNhSxbbeqsZ88ur8m8DGhQvvsh398NJ,
    rule_set_name: "Metaplex Royalty RuleSet Dev",
    operations: {
        "Delegate:Sale": All {
            rules: [
                Amount {
                    amount: 1,
                    operator: Eq,
                    field: "Amount",
                },
                ProgramOwnedList {
                    programs: [
                        metaqbxxUerdq28cj1RbAWkYQm3ybzjb6a8bt518x1s,
                        Roostrnex2Z9Y2XZC49sFAdZARP8E4iFpEnZC5QJWdz,
                    ],
                    field: "Delegate",
                },
            ],
        },
        "Delegate:LockedTransfer": All {
            rules: [
                Amount {
                    amount: 1,
                    operator: Eq,
                    field: "Amount",
                },
                ProgramOwnedList {
                    programs: [
                        metaqbxxUerdq28cj1RbAWkYQm3ybzjb6a8bt518x1s,
                        Roostrnex2Z9Y2XZC49sFAdZARP8E4iFpEnZC5QJWdz,
                    ],
                    field: "Delegate",
                },
            ],
        },
        "Delegate:Use": All {
            rules: [
                Amount {
                    amount: 1,
                    operator: Eq,
                    field: "Amount",
                },
                ProgramOwnedList {
                    programs: [
                        metaqbxxUerdq28cj1RbAWkYQm3ybzjb6a8bt518x1s,
                        Roostrnex2Z9Y2XZC49sFAdZARP8E4iFpEnZC5QJWdz,
                    ],
                    field: "Delegate",
                },
            ],
        },
        "Transfer:Owner": All {
            rules: [
                Amount {
                    amount: 1,
                    operator: Eq,
                    field: "Amount",
                },
                Any {
                    rules: [
                        ProgramOwnedList {
                            programs: [
                                metaqbxxUerdq28cj1RbAWkYQm3ybzjb6a8bt518x1s,
                                Roostrnex2Z9Y2XZC49sFAdZARP8E4iFpEnZC5QJWdz,
                            ],
                            field: "Source",
                        },
                        ProgramOwnedList {
                            programs: [
                                metaqbxxUerdq28cj1RbAWkYQm3ybzjb6a8bt518x1s,
                                Roostrnex2Z9Y2XZC49sFAdZARP8E4iFpEnZC5QJWdz,
                            ],
                            field: "Destination",
                        },
                        ProgramOwnedList {
                            programs: [
                                metaqbxxUerdq28cj1RbAWkYQm3ybzjb6a8bt518x1s,
                                Roostrnex2Z9Y2XZC49sFAdZARP8E4iFpEnZC5QJWdz,
                            ],
                            field: "Authority",
                        },
                    ],
                },
            ],
        },
        "Delegate:Collection": All {
            rules: [
                Amount {
                    amount: 1,
                    operator: Eq,
                    field: "Amount",
                },
                ProgramOwnedList {
                    programs: [
                        metaqbxxUerdq28cj1RbAWkYQm3ybzjb6a8bt518x1s,
                        Roostrnex2Z9Y2XZC49sFAdZARP8E4iFpEnZC5QJWdz,
                    ],
                    field: "Delegate",
                },
            ],
        },
        "Delegate:Staking": All {
            rules: [
                Amount {
                    amount: 1,
                    operator: Eq,
                    field: "Amount",
                },
                ProgramOwnedList {
                    programs: [
                        metaqbxxUerdq28cj1RbAWkYQm3ybzjb6a8bt518x1s,
                        Roostrnex2Z9Y2XZC49sFAdZARP8E4iFpEnZC5QJWdz,
                    ],
                    field: "Delegate",
                },
            ],
        },
        "Transfer:MigrationDelegate": All {
            rules: [
                Amount {
                    amount: 1,
                    operator: Eq,
                    field: "Amount",
                },
                Any {
                    rules: [
                        ProgramOwnedList {
                            programs: [
                                metaqbxxUerdq28cj1RbAWkYQm3ybzjb6a8bt518x1s,
                                Roostrnex2Z9Y2XZC49sFAdZARP8E4iFpEnZC5QJWdz,
                            ],
                            field: "Source",
                        },
                        ProgramOwnedList {
                            programs: [
                                metaqbxxUerdq28cj1RbAWkYQm3ybzjb6a8bt518x1s,
                                Roostrnex2Z9Y2XZC49sFAdZARP8E4iFpEnZC5QJWdz,
                            ],
                            field: "Destination",
                        },
                        ProgramOwnedList {
                            programs: [
                                metaqbxxUerdq28cj1RbAWkYQm3ybzjb6a8bt518x1s,
                                Roostrnex2Z9Y2XZC49sFAdZARP8E4iFpEnZC5QJWdz,
                            ],
                            field: "Authority",
                        },
                    ],
                },
            ],
        },
        "Transfer:SaleDelegate": All {
            rules: [
                Amount {
                    amount: 1,
                    operator: Eq,
                    field: "Amount",
                },
                Any {
                    rules: [
                        ProgramOwnedList {
                            programs: [
                                metaqbxxUerdq28cj1RbAWkYQm3ybzjb6a8bt518x1s,
                                Roostrnex2Z9Y2XZC49sFAdZARP8E4iFpEnZC5QJWdz,
                            ],
                            field: "Source",
                        },
                        ProgramOwnedList {
                            programs: [
                                metaqbxxUerdq28cj1RbAWkYQm3ybzjb6a8bt518x1s,
                                Roostrnex2Z9Y2XZC49sFAdZARP8E4iFpEnZC5QJWdz,
                            ],
                            field: "Destination",
                        },
                        ProgramOwnedList {
                            programs: [
                                metaqbxxUerdq28cj1RbAWkYQm3ybzjb6a8bt518x1s,
                                Roostrnex2Z9Y2XZC49sFAdZARP8E4iFpEnZC5QJWdz,
                            ],
                            field: "Authority",
                        },
                    ],
                },
            ],
        },
        "Delegate:Authority": All {
            rules: [
                Amount {
                    amount: 1,
                    operator: Eq,
                    field: "Amount",
                },
                ProgramOwnedList {
                    programs: [
                        metaqbxxUerdq28cj1RbAWkYQm3ybzjb6a8bt518x1s,
                        Roostrnex2Z9Y2XZC49sFAdZARP8E4iFpEnZC5QJWdz,
                    ],
                    field: "Delegate",
                },
            ],
        },
        "Delegate:Utility": All {
            rules: [
                Amount {
                    amount: 1,
                    operator: Eq,
                    field: "Amount",
                },
                ProgramOwnedList {
                    programs: [
                        metaqbxxUerdq28cj1RbAWkYQm3ybzjb6a8bt518x1s,
                        Roostrnex2Z9Y2XZC49sFAdZARP8E4iFpEnZC5QJWdz,
                    ],
                    field: "Delegate",
                },
            ],
        },
        "Delegate:Transfer": All {
            rules: [
                Amount {
                    amount: 1,
                    operator: Eq,
                    field: "Amount",
                },
                ProgramOwnedList {
                    programs: [
                        metaqbxxUerdq28cj1RbAWkYQm3ybzjb6a8bt518x1s,
                        Roostrnex2Z9Y2XZC49sFAdZARP8E4iFpEnZC5QJWdz,
                    ],
                    field: "Delegate",
                },
            ],
        },
        "Transfer:TransferDelegate": All {
            rules: [
                Amount {
                    amount: 1,
                    operator: Eq,
                    field: "Amount",
                },
                Any {
                    rules: [
                        ProgramOwnedList {
                            programs: [
                                metaqbxxUerdq28cj1RbAWkYQm3ybzjb6a8bt518x1s,
                                Roostrnex2Z9Y2XZC49sFAdZARP8E4iFpEnZC5QJWdz,
                            ],
                            field: "Source",
                        },
                        ProgramOwnedList {
                            programs: [
                                metaqbxxUerdq28cj1RbAWkYQm3ybzjb6a8bt518x1s,
                                Roostrnex2Z9Y2XZC49sFAdZARP8E4iFpEnZC5QJWdz,
                            ],
                            field: "Destination",
                        },
                        ProgramOwnedList {
                            programs: [
                                metaqbxxUerdq28cj1RbAWkYQm3ybzjb6a8bt518x1s,
                                Roostrnex2Z9Y2XZC49sFAdZARP8E4iFpEnZC5QJWdz,
                            ],
                            field: "Authority",
                        },
                    ],
                },
            ],
        },
        "Transfer:WalletToWallet": All {
            rules: [
                Amount {
                    amount: 1,
                    operator: Eq,
                    field: "Amount",
                },
                IsWallet {
                    field: "Source",
                },
                IsWallet {
                    field: "Destination",
                },
            ],
        },
        "Delegate:Update": All {
            rules: [
                Amount {
                    amount: 1,
                    operator: Eq,
                    field: "Amount",
                },
                ProgramOwnedList {
                    programs: [
                        metaqbxxUerdq28cj1RbAWkYQm3ybzjb6a8bt518x1s,
                        Roostrnex2Z9Y2XZC49sFAdZARP8E4iFpEnZC5QJWdz,
                    ],
                    field: "Delegate",
                },
            ],
        },
    },
}
TX Length: 679
Buffer tx signature: 623k31cpyDFz5xiYnciwMwRRueTkJfPHDpKWyDNeXEaPx4W87sMzYsoWhmuij5jAY84EH62fofAzvmFtjcu6fWZt
TX Length: 679
Buffer tx signature: 5FcbgDBU9LHU6aCE4bKmcWFP5MLgmVzswCp27txsVmwTThAuaUpu49Uy4WwpQaSwgxCbCXGQF2sFznVc4XsT7isY
TX Length: 679
Buffer tx signature: 4mQxb1fLHzc6CfVFQKgbb9K1xTZXypisNmPGjM3vuAh3nDzZdq6QYEUrMLNhCGSxqe3vvyLeEQuC3CUprFwd3acX
TX Length: 679
Buffer tx signature: U6cCMtXE6e7aGLVCsEpQfa4HeZiT99Vjd9srPCT6wkVJ18RLjAD5kd5YcZHXAYtNj5o5JRiqTKswFoXzWG2bj3q
TX Length: 679
Buffer tx signature: 2Pou3HwpSGhgFBXFtjppXHJJXMJRanBiLBvNQFY6X48YPhkbRaKdv8SRLCny5AhDLvNjtyqRU9kxyDtEcFtnU1mo
TX Length: 679
Buffer tx signature: 3xCZQm1rXQG2hycfc8WUQSdv2XC6yoSjeePRTiCfdk9R5Q22HAyHeEPe1ABMk6NXUrwS7JPGNGmi6eAS1FMDsom7
TX Length: 656
Buffer tx signature: 3X2rde2fDQ8AGLCrZyrPatWys7QuGHsksZFovWeZcjAJkPGPRHhFeNHtwF6mUhbYYGmrfEuus8tjzgcRKb6F1yWN
Create tx signature: 4jBnNkUtDvoynqn5bt22pxY464kQQxf9NVZRuUqBFvZESBkHweYCuDTq3CQX3S4cW3DmjM6amm2MNe1dKq4FaydW
```


