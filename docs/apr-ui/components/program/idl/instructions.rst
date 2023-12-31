components/program/idl/instructions.tsx
=======================================

Last edited: 2022-09-30 13:07:41

Contents:

.. code-block:: tsx

    import { memo } from "react";

import renderArguments from "../../../utils/renderArguments";

function renderAccounts(accounts) {
  let component = [];

  for (let i = 0; i < accounts.length; i++) {
    component.push(
      <div className="flex gap-2 pb-1" key={accounts[i].name}>
        <span>{accounts[i].name}</span>
        <div className="flex gap-1">
          {accounts[i].isSigner && (
            <span className="inline-flex items-center rounded bg-orange-100 px-2 py-0.5 text-xs font-medium text-orange-800">
              isSigner
            </span>
          )}
          {accounts[i].isMut && (
            <span className="inline-flex items-center rounded bg-green-100 px-2 py-0.5 text-xs font-medium text-green-800">
              isMut
            </span>
          )}
        </div>
      </div>
    );
  }

  return component;
}

function Instructions({ data }: InstructionsProps) {
  return (
    <div className="mt-5 flex flex-col">
      <div className="-my-2 -mx-4 overflow-x-auto sm:-mx-6 lg:-mx-8">
        <div className="inline-block min-w-full py-2 align-middle md:px-6 lg:px-8">
          <div className="overflow-hidden shadow ring-1 ring-black ring-opacity-5 md:rounded-lg">
            <table className="min-w-full divide-y divide-gray-300">
              <thead className="bg-gray-50">
                <tr>
                  <th
                    scope="col"
                    className="py-3 pl-4 pr-3 text-left text-xs font-medium uppercase tracking-wide text-gray-500 sm:pl-6"
                  >
                    Name
                  </th>
                  <th
                    scope="col"
                    className="px-3 py-3 text-left text-xs font-medium uppercase tracking-wide text-gray-500"
                  >
                    Arguments
                  </th>
                  <th
                    scope="col"
                    className="px-3 py-3 text-left text-xs font-medium uppercase tracking-wide text-gray-500"
                  >
                    Accounts
                  </th>
                </tr>
              </thead>
              <tbody className="prose divide-y divide-gray-200 bg-white">
                {data.map((item) => (
                  <tr key={item.name}>
                    <td className="whitespace-nowrap py-4 pl-4 pr-3 font-mono text-sm text-gray-500 sm:pl-6">
                      {item.name}
                    </td>
                    <td className="whitespace-nowrap px-3 py-4 font-mono text-sm text-gray-500">
                      {renderArguments(item.args)}
                    </td>
                    <td className="whitespace-nowrap px-3 py-4 font-mono text-sm text-gray-500">
                      {renderAccounts(item.accounts)}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  );
}

interface InstructionsProps {
  data: any;
}

export default memo(Instructions);


