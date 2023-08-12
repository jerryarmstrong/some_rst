components/program/tabs.tsx
===========================

Last edited: 2022-09-30 13:07:41

Contents:

.. code-block:: tsx

    import { memo } from "react";
import useSWR from "swr";
import dynamic from "next/dynamic";
import { useRouter } from "next/router";
import fetcher from "../../utils/fetcher";
import { Address, Idl } from "@project-serum/anchor";

const Readme = dynamic(() => import("./readme"));
const Builds = dynamic(() => import("./builds"));
const IdlViewer = dynamic(() => import("./idl-viewer"));
const SourceFiles = dynamic(() => import("./source-files"));
const AccountsData = dynamic(() => import("./accounts-data"));

function classNames(...classes) {
  return classes.filter(Boolean).join(" ");
}

function Tabs({
  tabs,
  selectedBuild,
  builds,
  readme,
  files,
  networkIdl,
  idlAddress,
}: TabsProps) {
  const router = useRouter();
  const { data: apiIdl } = useSWR(
    selectedBuild && (selectedBuild.artifacts.idl as string),
    fetcher
  );

  const idl = apiIdl || networkIdl;
  const address = selectedBuild?.address || idlAddress;

  let selectedTab = router.query.tab || "Readme";

  if (router.pathname.includes("/idl/")) {
    selectedTab = router.query.tab == "Accounts Data" ? "Accounts Data" : "IDL";
  }

  const idlHasAccount =
    idl && Array.isArray(idl.accounts) && idl.accounts.length > 0;

  return (
    <div>
      <div className="sm:hidden ">
        <div className="border-b border-gray-200 pb-4">
          <label htmlFor="tabs" className="sr-only">
            Select a tab
          </label>
          <select
            id="tabs"
            name="tabs"
            className="block w-full rounded-md border-gray-300 focus:border-amber-500 focus:ring-amber-500"
            defaultValue={tabs.find((tab) => tab.name === selectedTab).name}
          >
            {tabs.map((tab) => (
              <option key={tab.name}>{tab.name}</option>
            ))}
          </select>
        </div>
      </div>
      <div className="hidden sm:block">
        <div className="border-b border-gray-200">
          <nav className="-mb-px flex space-x-8" aria-label="Tabs">
            {tabs.map((tab) => (
              <button
                key={tab.name}
                onClick={() => {
                  let section = router.pathname.includes("/idl/")
                    ? "idl"
                    : "program";

                  router.push(
                    `/${section}/${router.query.address}?tab=${tab.name}`
                  );
                }}
                disabled={
                  tab.disabled ||
                  (tab.name === "IDL" && !idl) ||
                  (tab.name === "Accounts Data" && !idlHasAccount)
                }
                className={classNames(
                  tab.name === selectedTab
                    ? "border-amber-500 text-amber-600"
                    : "border-transparent text-gray-500 hover:border-gray-300 hover:text-gray-700",
                  "group inline-flex items-center border-b-2 py-4 px-1 text-sm font-medium disabled:cursor-not-allowed disabled:text-gray-300"
                )}
                aria-current={tab.name === selectedTab ? "page" : undefined}
              >
                <tab.icon
                  className={classNames(
                    tab.name === selectedTab
                      ? "text-amber-500"
                      : "text-gray-400 group-hover:text-gray-500",
                    tab.disabled && "text-gray-300 group-hover:text-gray-300",
                    (tab.name === "IDL" || tab.name === "Accounts Data") &&
                      !idl &&
                      "text-gray-300 group-hover:text-gray-300",
                    "-ml-0.5 mr-2 h-5 w-5"
                  )}
                  aria-hidden="true"
                />
                <span>{tab.name}</span>
              </button>
            ))}
          </nav>
        </div>
      </div>

      {selectedTab === "Readme" && <Readme readme={readme} />}
      {selectedTab === "Builds" && <Builds builds={builds} />}
      {selectedTab === "Explorer" && (
        <SourceFiles name={selectedBuild.name} files={files} readme={readme} />
      )}
      {selectedTab === "IDL" && (idl || networkIdl) && (
        <IdlViewer data={idl} url={selectedBuild?.artifacts?.idl} />
      )}
      {selectedTab === "Accounts Data" && idl && idl.accounts && (
        <AccountsData idl={idl} programID={address} />
      )}
    </div>
  );
}

interface TabsProps {
  readme: string | undefined;
  selectedBuild: any | undefined;
  builds: any[] | undefined;
  files: string[] | undefined;
  tabs: any[];
  networkIdl: Idl | undefined;
  idlAddress: Address | undefined;
}

export default memo(Tabs);


