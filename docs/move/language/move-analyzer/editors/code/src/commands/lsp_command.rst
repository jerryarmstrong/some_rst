language/move-analyzer/editors/code/src/commands/lsp_command.ts
===============================================================

Last edited: 2023-08-11 19:18:44

Contents:

.. code-block:: ts

    import type {
    DocumentSymbolParams,
    SymbolInformation,
    DocumentSymbol,
    CompletionParams,
    CompletionList,
    CompletionItem,
} from 'vscode-languageclient';
import { DocumentSymbolRequest, HoverRequest, CompletionRequest } from 'vscode-languageclient';
import type { Context } from '../context';

/**
 * An LSP command textDocument/documentSymbol
 */
export async function textDocumentDocumentSymbol(
    context: Readonly<Context>,
    params: DocumentSymbolParams,
): Promise<SymbolInformation[] | DocumentSymbol[] | null> {
    const client = context.getClient();
    if (client === undefined) {
        return Promise.reject(new Error('No language client connected.'));
    }

    // Send the request to the language client.
    return client.sendRequest(DocumentSymbolRequest.type, params);
}

/**
 * An LSP command textDocument/completion
 */
export async function textDocumentCompletion(
    context: Readonly<Context>,
    params: CompletionParams,
): Promise<CompletionList | CompletionItem[] | null> {
    const client = context.getClient();
    if (client === undefined) {
        return Promise.reject(new Error('No language client connected.'));
    }

    // Send the request to the language client.
    return client.sendRequest(CompletionRequest.type, params);
}


/**
 * An LSP command textDocument/hover
 */
export async function textDocumentHover(
    context: Readonly<Context>,
    params: DocumentSymbolParams,
)
    : Promise<SymbolInformation[] | DocumentSymbol[] | null> {
    const client = context.getClient();
    if (client === undefined) {
        return Promise.reject(new Error('No language client connected.'));
    }

    // Send the request to the language client.
    return client.sendRequest(HoverRequest.method, params);
}


