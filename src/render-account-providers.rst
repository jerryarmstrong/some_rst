src/render-account-providers.ts
===============================

Last edited: 2023-07-06 15:09:22

Contents:

.. code-block:: ts

    import { IdlAccount } from './types'

class AccountProvidersRenderer {
  private readonly upperCamelCaseAccountNames: string[]
  constructor(accounts: IdlAccount[]) {
    this.upperCamelCaseAccountNames = accounts.map((account) =>
      account.name.charAt(0).toUpperCase().concat(account.name.slice(1))
    )
  }

  _renderImports() {
    return this.upperCamelCaseAccountNames
      .map((account) => `import { ${account} } from './${account}'`)
      .join('\n')
  }

  _renderProviders() {
    return `export const accountProviders = { ${this.upperCamelCaseAccountNames.join(
      ', '
    )} }`
  }

  render() {
    if (this.upperCamelCaseAccountNames.length === 0) return ''
    return `
${this._renderImports()}

${this._renderProviders()}
`.trim()
  }
}

/*
 * Renders imports of all accounts and re-export as account providers assuming
 * that this code will live in a module located in the same folder as the
 * account modules.
 */
export function renderAccountProviders(accounts?: IdlAccount[]) {
  return new AccountProvidersRenderer(accounts ?? []).render()
}


