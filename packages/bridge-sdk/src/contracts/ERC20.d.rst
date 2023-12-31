packages/bridge-sdk/src/contracts/ERC20.d.ts
============================================

Last edited: 2023-07-19 16:40:40

Contents:

.. code-block:: ts

    /* Autogenerated file. Do not edit manually. */
/* tslint:disable */
/* eslint-disable */

import { Contract, ContractTransaction, EventFilter, Signer } from 'ethers';
import { Listener, Provider } from 'ethers/providers';
import { Arrayish, BigNumber, BigNumberish, Interface } from 'ethers/utils';
import {
  TransactionOverrides,
  TypedEventDescription,
  TypedFunctionDescription,
} from '.';

interface ERC20Interface extends Interface {
  functions: {
    name: TypedFunctionDescription<{ encode([]: []): string }>;

    symbol: TypedFunctionDescription<{ encode([]: []): string }>;

    decimals: TypedFunctionDescription<{ encode([]: []): string }>;

    totalSupply: TypedFunctionDescription<{ encode([]: []): string }>;

    balanceOf: TypedFunctionDescription<{
      encode([account]: [string]): string;
    }>;

    transfer: TypedFunctionDescription<{
      encode([recipient, amount]: [string, BigNumberish]): string;
    }>;

    allowance: TypedFunctionDescription<{
      encode([owner, spender]: [string, string]): string;
    }>;

    approve: TypedFunctionDescription<{
      encode([spender, amount]: [string, BigNumberish]): string;
    }>;

    transferFrom: TypedFunctionDescription<{
      encode([sender, recipient, amount]: [
        string,
        string,
        BigNumberish,
      ]): string;
    }>;

    increaseAllowance: TypedFunctionDescription<{
      encode([spender, addedValue]: [string, BigNumberish]): string;
    }>;

    decreaseAllowance: TypedFunctionDescription<{
      encode([spender, subtractedValue]: [string, BigNumberish]): string;
    }>;
  };

  events: {
    Approval: TypedEventDescription<{
      encodeTopics([owner, spender, value]: [
        string | null,
        string | null,
        null,
      ]): string[];
    }>;

    Transfer: TypedEventDescription<{
      encodeTopics([from, to, value]: [
        string | null,
        string | null,
        null,
      ]): string[];
    }>;
  };
}

export class ERC20 extends Contract {
  connect(signerOrProvider: Signer | Provider | string): ERC20;
  attach(addressOrName: string): ERC20;
  deployed(): Promise<ERC20>;

  on(event: EventFilter | string, listener: Listener): ERC20;
  once(event: EventFilter | string, listener: Listener): ERC20;
  addListener(eventName: EventFilter | string, listener: Listener): ERC20;
  removeAllListeners(eventName: EventFilter | string): ERC20;
  removeListener(eventName: any, listener: Listener): ERC20;

  interface: ERC20Interface;

  functions: {
    /**
     * Returns the name of the token.
     */
    name(overrides?: TransactionOverrides): Promise<string>;

    /**
     * Returns the name of the token.
     */
    'name()'(overrides?: TransactionOverrides): Promise<string>;

    /**
     * Returns the symbol of the token, usually a shorter version of the name.
     */
    symbol(overrides?: TransactionOverrides): Promise<string>;

    /**
     * Returns the symbol of the token, usually a shorter version of the name.
     */
    'symbol()'(overrides?: TransactionOverrides): Promise<string>;

    /**
     * Returns the number of decimals used to get its user representation. For example, if `decimals` equals `2`, a balance of `505` tokens should be displayed to a user as `5,05` (`505 / 10 ** 2`). Tokens usually opt for a value of 18, imitating the relationship between Ether and Wei. This is the value {ERC20} uses, unless {_setupDecimals} is called. NOTE: This information is only used for _display_ purposes: it in no way affects any of the arithmetic of the contract, including {IERC20-balanceOf} and {IERC20-transfer}.
     */
    decimals(overrides?: TransactionOverrides): Promise<number>;

    /**
     * Returns the number of decimals used to get its user representation. For example, if `decimals` equals `2`, a balance of `505` tokens should be displayed to a user as `5,05` (`505 / 10 ** 2`). Tokens usually opt for a value of 18, imitating the relationship between Ether and Wei. This is the value {ERC20} uses, unless {_setupDecimals} is called. NOTE: This information is only used for _display_ purposes: it in no way affects any of the arithmetic of the contract, including {IERC20-balanceOf} and {IERC20-transfer}.
     */
    'decimals()'(overrides?: TransactionOverrides): Promise<number>;

    /**
     * See {IERC20-totalSupply}.
     */
    totalSupply(overrides?: TransactionOverrides): Promise<BigNumber>;

    /**
     * See {IERC20-totalSupply}.
     */
    'totalSupply()'(overrides?: TransactionOverrides): Promise<BigNumber>;

    /**
     * See {IERC20-balanceOf}.
     */
    balanceOf(
      account: string,
      overrides?: TransactionOverrides,
    ): Promise<BigNumber>;

    /**
     * See {IERC20-balanceOf}.
     */
    'balanceOf(address)'(
      account: string,
      overrides?: TransactionOverrides,
    ): Promise<BigNumber>;

    /**
     * See {IERC20-transfer}. Requirements: - `recipient` cannot be the zero address. - the caller must have a balance of at least `amount`.
     */
    transfer(
      recipient: string,
      amount: BigNumberish,
      overrides?: TransactionOverrides,
    ): Promise<ContractTransaction>;

    /**
     * See {IERC20-transfer}. Requirements: - `recipient` cannot be the zero address. - the caller must have a balance of at least `amount`.
     */
    'transfer(address,uint256)'(
      recipient: string,
      amount: BigNumberish,
      overrides?: TransactionOverrides,
    ): Promise<ContractTransaction>;

    /**
     * See {IERC20-allowance}.
     */
    allowance(
      owner: string,
      spender: string,
      overrides?: TransactionOverrides,
    ): Promise<BigNumber>;

    /**
     * See {IERC20-allowance}.
     */
    'allowance(address,address)'(
      owner: string,
      spender: string,
      overrides?: TransactionOverrides,
    ): Promise<BigNumber>;

    /**
     * See {IERC20-approve}. Requirements: - `spender` cannot be the zero address.
     */
    approve(
      spender: string,
      amount: BigNumberish,
      overrides?: TransactionOverrides,
    ): Promise<ContractTransaction>;

    /**
     * See {IERC20-approve}. Requirements: - `spender` cannot be the zero address.
     */
    'approve(address,uint256)'(
      spender: string,
      amount: BigNumberish,
      overrides?: TransactionOverrides,
    ): Promise<ContractTransaction>;

    /**
     * See {IERC20-transferFrom}. Emits an {Approval} event indicating the updated allowance. This is not required by the EIP. See the note at the beginning of {ERC20}. Requirements: - `sender` and `recipient` cannot be the zero address. - `sender` must have a balance of at least `amount`. - the caller must have allowance for ``sender``'s tokens of at least `amount`.
     */
    transferFrom(
      sender: string,
      recipient: string,
      amount: BigNumberish,
      overrides?: TransactionOverrides,
    ): Promise<ContractTransaction>;

    /**
     * See {IERC20-transferFrom}. Emits an {Approval} event indicating the updated allowance. This is not required by the EIP. See the note at the beginning of {ERC20}. Requirements: - `sender` and `recipient` cannot be the zero address. - `sender` must have a balance of at least `amount`. - the caller must have allowance for ``sender``'s tokens of at least `amount`.
     */
    'transferFrom(address,address,uint256)'(
      sender: string,
      recipient: string,
      amount: BigNumberish,
      overrides?: TransactionOverrides,
    ): Promise<ContractTransaction>;

    /**
     * Atomically increases the allowance granted to `spender` by the caller. This is an alternative to {approve} that can be used as a mitigation for problems described in {IERC20-approve}. Emits an {Approval} event indicating the updated allowance. Requirements: - `spender` cannot be the zero address.
     */
    increaseAllowance(
      spender: string,
      addedValue: BigNumberish,
      overrides?: TransactionOverrides,
    ): Promise<ContractTransaction>;

    /**
     * Atomically increases the allowance granted to `spender` by the caller. This is an alternative to {approve} that can be used as a mitigation for problems described in {IERC20-approve}. Emits an {Approval} event indicating the updated allowance. Requirements: - `spender` cannot be the zero address.
     */
    'increaseAllowance(address,uint256)'(
      spender: string,
      addedValue: BigNumberish,
      overrides?: TransactionOverrides,
    ): Promise<ContractTransaction>;

    /**
     * Atomically decreases the allowance granted to `spender` by the caller. This is an alternative to {approve} that can be used as a mitigation for problems described in {IERC20-approve}. Emits an {Approval} event indicating the updated allowance. Requirements: - `spender` cannot be the zero address. - `spender` must have allowance for the caller of at least `subtractedValue`.
     */
    decreaseAllowance(
      spender: string,
      subtractedValue: BigNumberish,
      overrides?: TransactionOverrides,
    ): Promise<ContractTransaction>;

    /**
     * Atomically decreases the allowance granted to `spender` by the caller. This is an alternative to {approve} that can be used as a mitigation for problems described in {IERC20-approve}. Emits an {Approval} event indicating the updated allowance. Requirements: - `spender` cannot be the zero address. - `spender` must have allowance for the caller of at least `subtractedValue`.
     */
    'decreaseAllowance(address,uint256)'(
      spender: string,
      subtractedValue: BigNumberish,
      overrides?: TransactionOverrides,
    ): Promise<ContractTransaction>;
  };

  /**
   * Returns the name of the token.
   */
  name(overrides?: TransactionOverrides): Promise<string>;

  /**
   * Returns the name of the token.
   */
  'name()'(overrides?: TransactionOverrides): Promise<string>;

  /**
   * Returns the symbol of the token, usually a shorter version of the name.
   */
  symbol(overrides?: TransactionOverrides): Promise<string>;

  /**
   * Returns the symbol of the token, usually a shorter version of the name.
   */
  'symbol()'(overrides?: TransactionOverrides): Promise<string>;

  /**
   * Returns the number of decimals used to get its user representation. For example, if `decimals` equals `2`, a balance of `505` tokens should be displayed to a user as `5,05` (`505 / 10 ** 2`). Tokens usually opt for a value of 18, imitating the relationship between Ether and Wei. This is the value {ERC20} uses, unless {_setupDecimals} is called. NOTE: This information is only used for _display_ purposes: it in no way affects any of the arithmetic of the contract, including {IERC20-balanceOf} and {IERC20-transfer}.
   */
  decimals(overrides?: TransactionOverrides): Promise<number>;

  /**
   * Returns the number of decimals used to get its user representation. For example, if `decimals` equals `2`, a balance of `505` tokens should be displayed to a user as `5,05` (`505 / 10 ** 2`). Tokens usually opt for a value of 18, imitating the relationship between Ether and Wei. This is the value {ERC20} uses, unless {_setupDecimals} is called. NOTE: This information is only used for _display_ purposes: it in no way affects any of the arithmetic of the contract, including {IERC20-balanceOf} and {IERC20-transfer}.
   */
  'decimals()'(overrides?: TransactionOverrides): Promise<number>;

  /**
   * See {IERC20-totalSupply}.
   */
  totalSupply(overrides?: TransactionOverrides): Promise<BigNumber>;

  /**
   * See {IERC20-totalSupply}.
   */
  'totalSupply()'(overrides?: TransactionOverrides): Promise<BigNumber>;

  /**
   * See {IERC20-balanceOf}.
   */
  balanceOf(
    account: string,
    overrides?: TransactionOverrides,
  ): Promise<BigNumber>;

  /**
   * See {IERC20-balanceOf}.
   */
  'balanceOf(address)'(
    account: string,
    overrides?: TransactionOverrides,
  ): Promise<BigNumber>;

  /**
   * See {IERC20-transfer}. Requirements: - `recipient` cannot be the zero address. - the caller must have a balance of at least `amount`.
   */
  transfer(
    recipient: string,
    amount: BigNumberish,
    overrides?: TransactionOverrides,
  ): Promise<ContractTransaction>;

  /**
   * See {IERC20-transfer}. Requirements: - `recipient` cannot be the zero address. - the caller must have a balance of at least `amount`.
   */
  'transfer(address,uint256)'(
    recipient: string,
    amount: BigNumberish,
    overrides?: TransactionOverrides,
  ): Promise<ContractTransaction>;

  /**
   * See {IERC20-allowance}.
   */
  allowance(
    owner: string,
    spender: string,
    overrides?: TransactionOverrides,
  ): Promise<BigNumber>;

  /**
   * See {IERC20-allowance}.
   */
  'allowance(address,address)'(
    owner: string,
    spender: string,
    overrides?: TransactionOverrides,
  ): Promise<BigNumber>;

  /**
   * See {IERC20-approve}. Requirements: - `spender` cannot be the zero address.
   */
  approve(
    spender: string,
    amount: BigNumberish,
    overrides?: TransactionOverrides,
  ): Promise<ContractTransaction>;

  /**
   * See {IERC20-approve}. Requirements: - `spender` cannot be the zero address.
   */
  'approve(address,uint256)'(
    spender: string,
    amount: BigNumberish,
    overrides?: TransactionOverrides,
  ): Promise<ContractTransaction>;

  /**
   * See {IERC20-transferFrom}. Emits an {Approval} event indicating the updated allowance. This is not required by the EIP. See the note at the beginning of {ERC20}. Requirements: - `sender` and `recipient` cannot be the zero address. - `sender` must have a balance of at least `amount`. - the caller must have allowance for ``sender``'s tokens of at least `amount`.
   */
  transferFrom(
    sender: string,
    recipient: string,
    amount: BigNumberish,
    overrides?: TransactionOverrides,
  ): Promise<ContractTransaction>;

  /**
   * See {IERC20-transferFrom}. Emits an {Approval} event indicating the updated allowance. This is not required by the EIP. See the note at the beginning of {ERC20}. Requirements: - `sender` and `recipient` cannot be the zero address. - `sender` must have a balance of at least `amount`. - the caller must have allowance for ``sender``'s tokens of at least `amount`.
   */
  'transferFrom(address,address,uint256)'(
    sender: string,
    recipient: string,
    amount: BigNumberish,
    overrides?: TransactionOverrides,
  ): Promise<ContractTransaction>;

  /**
   * Atomically increases the allowance granted to `spender` by the caller. This is an alternative to {approve} that can be used as a mitigation for problems described in {IERC20-approve}. Emits an {Approval} event indicating the updated allowance. Requirements: - `spender` cannot be the zero address.
   */
  increaseAllowance(
    spender: string,
    addedValue: BigNumberish,
    overrides?: TransactionOverrides,
  ): Promise<ContractTransaction>;

  /**
   * Atomically increases the allowance granted to `spender` by the caller. This is an alternative to {approve} that can be used as a mitigation for problems described in {IERC20-approve}. Emits an {Approval} event indicating the updated allowance. Requirements: - `spender` cannot be the zero address.
   */
  'increaseAllowance(address,uint256)'(
    spender: string,
    addedValue: BigNumberish,
    overrides?: TransactionOverrides,
  ): Promise<ContractTransaction>;

  /**
   * Atomically decreases the allowance granted to `spender` by the caller. This is an alternative to {approve} that can be used as a mitigation for problems described in {IERC20-approve}. Emits an {Approval} event indicating the updated allowance. Requirements: - `spender` cannot be the zero address. - `spender` must have allowance for the caller of at least `subtractedValue`.
   */
  decreaseAllowance(
    spender: string,
    subtractedValue: BigNumberish,
    overrides?: TransactionOverrides,
  ): Promise<ContractTransaction>;

  /**
   * Atomically decreases the allowance granted to `spender` by the caller. This is an alternative to {approve} that can be used as a mitigation for problems described in {IERC20-approve}. Emits an {Approval} event indicating the updated allowance. Requirements: - `spender` cannot be the zero address. - `spender` must have allowance for the caller of at least `subtractedValue`.
   */
  'decreaseAllowance(address,uint256)'(
    spender: string,
    subtractedValue: BigNumberish,
    overrides?: TransactionOverrides,
  ): Promise<ContractTransaction>;

  filters: {
    Approval(
      owner: string | null,
      spender: string | null,
      value: null,
    ): EventFilter;

    Transfer(from: string | null, to: string | null, value: null): EventFilter;
  };

  estimate: {
    /**
     * Returns the name of the token.
     */
    name(overrides?: TransactionOverrides): Promise<BigNumber>;

    /**
     * Returns the name of the token.
     */
    'name()'(overrides?: TransactionOverrides): Promise<BigNumber>;

    /**
     * Returns the symbol of the token, usually a shorter version of the name.
     */
    symbol(overrides?: TransactionOverrides): Promise<BigNumber>;

    /**
     * Returns the symbol of the token, usually a shorter version of the name.
     */
    'symbol()'(overrides?: TransactionOverrides): Promise<BigNumber>;

    /**
     * Returns the number of decimals used to get its user representation. For example, if `decimals` equals `2`, a balance of `505` tokens should be displayed to a user as `5,05` (`505 / 10 ** 2`). Tokens usually opt for a value of 18, imitating the relationship between Ether and Wei. This is the value {ERC20} uses, unless {_setupDecimals} is called. NOTE: This information is only used for _display_ purposes: it in no way affects any of the arithmetic of the contract, including {IERC20-balanceOf} and {IERC20-transfer}.
     */
    decimals(overrides?: TransactionOverrides): Promise<BigNumber>;

    /**
     * Returns the number of decimals used to get its user representation. For example, if `decimals` equals `2`, a balance of `505` tokens should be displayed to a user as `5,05` (`505 / 10 ** 2`). Tokens usually opt for a value of 18, imitating the relationship between Ether and Wei. This is the value {ERC20} uses, unless {_setupDecimals} is called. NOTE: This information is only used for _display_ purposes: it in no way affects any of the arithmetic of the contract, including {IERC20-balanceOf} and {IERC20-transfer}.
     */
    'decimals()'(overrides?: TransactionOverrides): Promise<BigNumber>;

    /**
     * See {IERC20-totalSupply}.
     */
    totalSupply(overrides?: TransactionOverrides): Promise<BigNumber>;

    /**
     * See {IERC20-totalSupply}.
     */
    'totalSupply()'(overrides?: TransactionOverrides): Promise<BigNumber>;

    /**
     * See {IERC20-balanceOf}.
     */
    balanceOf(
      account: string,
      overrides?: TransactionOverrides,
    ): Promise<BigNumber>;

    /**
     * See {IERC20-balanceOf}.
     */
    'balanceOf(address)'(
      account: string,
      overrides?: TransactionOverrides,
    ): Promise<BigNumber>;

    /**
     * See {IERC20-transfer}. Requirements: - `recipient` cannot be the zero address. - the caller must have a balance of at least `amount`.
     */
    transfer(
      recipient: string,
      amount: BigNumberish,
      overrides?: TransactionOverrides,
    ): Promise<BigNumber>;

    /**
     * See {IERC20-transfer}. Requirements: - `recipient` cannot be the zero address. - the caller must have a balance of at least `amount`.
     */
    'transfer(address,uint256)'(
      recipient: string,
      amount: BigNumberish,
      overrides?: TransactionOverrides,
    ): Promise<BigNumber>;

    /**
     * See {IERC20-allowance}.
     */
    allowance(
      owner: string,
      spender: string,
      overrides?: TransactionOverrides,
    ): Promise<BigNumber>;

    /**
     * See {IERC20-allowance}.
     */
    'allowance(address,address)'(
      owner: string,
      spender: string,
      overrides?: TransactionOverrides,
    ): Promise<BigNumber>;

    /**
     * See {IERC20-approve}. Requirements: - `spender` cannot be the zero address.
     */
    approve(
      spender: string,
      amount: BigNumberish,
      overrides?: TransactionOverrides,
    ): Promise<BigNumber>;

    /**
     * See {IERC20-approve}. Requirements: - `spender` cannot be the zero address.
     */
    'approve(address,uint256)'(
      spender: string,
      amount: BigNumberish,
      overrides?: TransactionOverrides,
    ): Promise<BigNumber>;

    /**
     * See {IERC20-transferFrom}. Emits an {Approval} event indicating the updated allowance. This is not required by the EIP. See the note at the beginning of {ERC20}. Requirements: - `sender` and `recipient` cannot be the zero address. - `sender` must have a balance of at least `amount`. - the caller must have allowance for ``sender``'s tokens of at least `amount`.
     */
    transferFrom(
      sender: string,
      recipient: string,
      amount: BigNumberish,
      overrides?: TransactionOverrides,
    ): Promise<BigNumber>;

    /**
     * See {IERC20-transferFrom}. Emits an {Approval} event indicating the updated allowance. This is not required by the EIP. See the note at the beginning of {ERC20}. Requirements: - `sender` and `recipient` cannot be the zero address. - `sender` must have a balance of at least `amount`. - the caller must have allowance for ``sender``'s tokens of at least `amount`.
     */
    'transferFrom(address,address,uint256)'(
      sender: string,
      recipient: string,
      amount: BigNumberish,
      overrides?: TransactionOverrides,
    ): Promise<BigNumber>;

    /**
     * Atomically increases the allowance granted to `spender` by the caller. This is an alternative to {approve} that can be used as a mitigation for problems described in {IERC20-approve}. Emits an {Approval} event indicating the updated allowance. Requirements: - `spender` cannot be the zero address.
     */
    increaseAllowance(
      spender: string,
      addedValue: BigNumberish,
      overrides?: TransactionOverrides,
    ): Promise<BigNumber>;

    /**
     * Atomically increases the allowance granted to `spender` by the caller. This is an alternative to {approve} that can be used as a mitigation for problems described in {IERC20-approve}. Emits an {Approval} event indicating the updated allowance. Requirements: - `spender` cannot be the zero address.
     */
    'increaseAllowance(address,uint256)'(
      spender: string,
      addedValue: BigNumberish,
      overrides?: TransactionOverrides,
    ): Promise<BigNumber>;

    /**
     * Atomically decreases the allowance granted to `spender` by the caller. This is an alternative to {approve} that can be used as a mitigation for problems described in {IERC20-approve}. Emits an {Approval} event indicating the updated allowance. Requirements: - `spender` cannot be the zero address. - `spender` must have allowance for the caller of at least `subtractedValue`.
     */
    decreaseAllowance(
      spender: string,
      subtractedValue: BigNumberish,
      overrides?: TransactionOverrides,
    ): Promise<BigNumber>;

    /**
     * Atomically decreases the allowance granted to `spender` by the caller. This is an alternative to {approve} that can be used as a mitigation for problems described in {IERC20-approve}. Emits an {Approval} event indicating the updated allowance. Requirements: - `spender` cannot be the zero address. - `spender` must have allowance for the caller of at least `subtractedValue`.
     */
    'decreaseAllowance(address,uint256)'(
      spender: string,
      subtractedValue: BigNumberish,
      overrides?: TransactionOverrides,
    ): Promise<BigNumber>;
  };
}


