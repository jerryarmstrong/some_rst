src/App.tsx
===========

Last edited: 2022-08-30 20:54:29

Contents:

.. code-block:: tsx

    import { Switch, Route, Redirect } from "react-router-dom";

import { ClusterModal } from "components/ClusterModal";
import { MessageBanner } from "components/MessageBanner";
import { Navbar } from "components/Navbar";
import { ClusterStatusBanner } from "components/ClusterStatusButton";
import { SearchBar } from "components/SearchBar";

import { AccountDetailsPage } from "pages/AccountDetailsPage";
import { TransactionInspectorPage } from "pages/inspector/InspectorPage";
import { ClusterStatsPage } from "pages/ClusterStatsPage";
import { SupplyPage } from "pages/SupplyPage";
import { TransactionDetailsPage } from "pages/TransactionDetailsPage";
import { BlockDetailsPage } from "pages/BlockDetailsPage";
import { EpochDetailsPage } from "pages/EpochDetailsPage";
import { AmmanGuidePage } from "amman/pages";

const ADDRESS_ALIASES = ["account", "accounts", "addresses"];
const TX_ALIASES = ["txs", "txn", "txns", "transaction", "transactions"];

function App(props: { ammanConnected: boolean }) {
  return (
    <>
      <ClusterModal />
      <div className="main-content pb-4">
        <Navbar />
        <MessageBanner />
        <ClusterStatusBanner />
        <SearchBar />
        <Switch>
          <Route
            exact
            path="/"
            render={({ location }) => {
              return props.ammanConnected ? (
                <Redirect to={{ ...location, pathname: "clusterStats" }} />
              ) : (
                <Redirect to={{ ...location, pathname: "guide" }} />
              );
            }}
          ></Route>
          <Route exact path={["/guide"]}>
            <AmmanGuidePage />
          </Route>
          <Route exact path={["/clusterStats"]}>
            <ClusterStatsPage />
          </Route>
          <Route exact path={["/supply", "/accounts", "accounts/top"]}>
            <SupplyPage />
          </Route>
          <Route
            exact
            path={TX_ALIASES.map((tx) => `/${tx}/:signature`)}
            render={({ match, location }) => {
              let pathname = `/tx/${match.params.signature}`;
              return <Redirect to={{ ...location, pathname }} />;
            }}
          />
          <Route
            exact
            path={["/tx/inspector", "/tx/:signature/inspect"]}
            render={({ match }) => (
              // @ts-ignore
              <TransactionInspectorPage signature={match.params.signature} />
            )}
          />
          <Route
            exact
            path={"/tx/:signature"}
            render={({ match }) => (
              <TransactionDetailsPage signature={match.params.signature} />
            )}
          />
          <Route
            exact
            path={"/epoch/:id"}
            render={({ match }) => <EpochDetailsPage epoch={match.params.id} />}
          />
          <Route
            exact
            path={["/block/:id", "/block/:id/:tab"]}
            render={({ match }) => (
              // @ts-ignore
              <BlockDetailsPage slot={match.params.id} tab={match.params.tab} />
            )}
          />
          <Route
            exact
            path={[
              ...ADDRESS_ALIASES.map((path) => `/${path}/:address`),
              ...ADDRESS_ALIASES.map((path) => `/${path}/:address/:tab`),
            ]}
            render={({ match, location }) => {
              let pathname = `/address/${match.params.address}`;
              if (match.params.tab) {
                pathname += `/${match.params.tab}`;
              }
              return <Redirect to={{ ...location, pathname }} />;
            }}
          />
          <Route
            exact
            path={["/address/:address", "/address/:address/:tab"]}
            render={({ match }) => (
              <AccountDetailsPage
                address={match.params.address}
                // @ts-ignore
                tab={match.params.tab}
              />
            )}
          />
        </Switch>
      </div>
    </>
  );
}

export default App;


