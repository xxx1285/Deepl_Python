class MydsLazyLoadScripts {
  constructor() {
    (this.v = "1.2.4"),
      (this.triggerEvents = [
        "keydown",
        "mousedown",
        "mousemove",
        "touchmove",
        "touchstart",
        "touchend",
        "wheel",
      ]),
      (this.userEventHandler = this._triggerListener.bind(this)),
      (this.touchStartHandler = this._onTouchStart.bind(this)),
      (this.touchMoveHandler = this._onTouchMove.bind(this)),
      (this.touchEndHandler = this._onTouchEnd.bind(this)),
      (this.clickHandler = this._onClick.bind(this)),
      (this.interceptedClicks = []),
      window.addEventListener("pageshow", (e) => {
        this.persisted = e.persisted;
      }),
      window.addEventListener("DOMContentLoaded", () => {
        this._preconnect3rdParties();
      }),
      (this.delayedScripts = { normal: [], async: [], defer: [] }),
      (this.trash = []),
      (this.allJQueries = []);
  }
  _addUserInteractionListener(e) {
    document.hidden
      ? e._triggerListener()
      : (this.triggerEvents.forEach((t) =>
          window.addEventListener(t, e.userEventHandler, { passive: !0 })
        ),
        window.addEventListener("touchstart", e.touchStartHandler, {
          passive: !0,
        }),
        window.addEventListener("mousedown", e.touchStartHandler),
        document.addEventListener("visibilitychange", e.userEventHandler));
  }
  _removeUserInteractionListener() {
    this.triggerEvents.forEach((e) =>
      window.removeEventListener(e, this.userEventHandler, { passive: !0 })
    ),
      document.removeEventListener("visibilitychange", this.userEventHandler);
  }
  _onTouchStart(e) {
    "HTML" !== e.target.tagName &&
      (window.addEventListener("touchend", this.touchEndHandler),
      window.addEventListener("mouseup", this.touchEndHandler),
      window.addEventListener("touchmove", this.touchMoveHandler, {
        passive: !0,
      }),
      window.addEventListener("mousemove", this.touchMoveHandler),
      e.target.addEventListener("click", this.clickHandler),
      this._renameDOMAttribute(e.target, "onclick", "myds-onclick"),
      this._pendingClickStarted());
  }
  _onTouchMove(e) {
    window.removeEventListener("touchend", this.touchEndHandler),
      window.removeEventListener("mouseup", this.touchEndHandler),
      window.removeEventListener("touchmove", this.touchMoveHandler, {
        passive: !0,
      }),
      window.removeEventListener("mousemove", this.touchMoveHandler),
      e.target.removeEventListener("click", this.clickHandler),
      this._renameDOMAttribute(e.target, "myds-onclick", "onclick"),
      this._pendingClickFinished();
  }
  _onTouchEnd(e) {
    window.removeEventListener("touchend", this.touchEndHandler),
      window.removeEventListener("mouseup", this.touchEndHandler),
      window.removeEventListener("touchmove", this.touchMoveHandler, {
        passive: !0,
      }),
      window.removeEventListener("mousemove", this.touchMoveHandler);
  }
  _onClick(e) {
    e.target.removeEventListener("click", this.clickHandler),
      this._renameDOMAttribute(e.target, "myds-onclick", "onclick"),
      this.interceptedClicks.push(e),
      e.preventDefault(),
      e.stopPropagation(),
      e.stopImmediatePropagation(),
      this._pendingClickFinished();
  }
  _replayClicks() {
    window.removeEventListener("touchstart", this.touchStartHandler, {
      passive: !0,
    }),
      window.removeEventListener("mousedown", this.touchStartHandler),
      this.interceptedClicks.forEach((e) => {
        e.target.dispatchEvent(
          new MouseEvent("click", { view: e.view, bubbles: !0, cancelable: !0 })
        );
      });
  }
  _waitForPendingClicks() {
    return new Promise((e) => {
      this._isClickPending ? (this._pendingClickFinished = e) : e();
    });
  }
  _pendingClickStarted() {
    this._isClickPending = !0;
  }
  _pendingClickFinished() {
    this._isClickPending = !1;
  }
  _renameDOMAttribute(e, t, i) {
    e.hasAttribute &&
      e.hasAttribute(t) &&
      (event.target.setAttribute(i, event.target.getAttribute(t)),
      event.target.removeAttribute(t));
  }
  _triggerListener() {
    this._removeUserInteractionListener(this),
      "loading" === document.readyState
        ? document.addEventListener(
            "DOMContentLoaded",
            this._loadEverythingNow.bind(this)
          )
        : this._loadEverythingNow();
  }
  _preconnect3rdParties() {
    let e = [];
    document
      .querySelectorAll("script[type=mydslazyloadscript]")
      .forEach((t) => {
        if (t.hasAttribute("src")) {
          let i = new URL(t.src).origin;
          i !== location.origin &&
            e.push({
              src: i,
              crossOrigin:
                t.crossOrigin || "module" === t.getAttribute("data-myds-type"),
            });
        }
      }),
      (e = [...new Map(e.map((e) => [JSON.stringify(e), e])).values()]),
      this._batchInjectResourceHints(e, "preconnect");
  }
  async _loadEverythingNow() {
    (this.lastBreath = Date.now()),
      this._delayEventListeners(this),
      this._delayJQueryReady(this),
      this._handleDocumentWrite(),
      this._registerAllDelayedScripts(),
      this._preloadAllScripts(),
      await this._loadScriptsFromList(this.delayedScripts.normal),
      await this._loadScriptsFromList(this.delayedScripts.defer),
      await this._loadScriptsFromList(this.delayedScripts.async);
    try {
      await this._triggerDOMContentLoaded(), await this._triggerWindowLoad();
    } catch (e) {
      console.error(e);
    }
    window.dispatchEvent(new Event("myds-allScriptsLoaded")),
      this._waitForPendingClicks().then(() => {
        this._replayClicks();
      }),
      this._emptyTrash();
  }
  _registerAllDelayedScripts() {
    document
      .querySelectorAll("script[type=mydslazyloadscript]")
      .forEach((e) => {
        e.hasAttribute("data-myds-src")
          ? e.hasAttribute("async") && !1 !== e.async
            ? this.delayedScripts.async.push(e)
            : (e.hasAttribute("defer") && !1 !== e.defer) ||
              "module" === e.getAttribute("data-myds-type")
            ? this.delayedScripts.defer.push(e)
            : this.delayedScripts.normal.push(e)
          : this.delayedScripts.normal.push(e);
      });
  }
  async _transformScript(e) {
    return new Promise(
      (await this._littleBreath(),
      navigator.userAgent.indexOf("Firefox/") > 0 || "" === navigator.vendor
        ? (t) => {
            let i = document.createElement("script");
            [...e.attributes].forEach((e) => {
              let t = e.nodeName;
              "type" !== t &&
                ("data-myds-type" === t && (t = "type"),
                "data-myds-src" === t && (t = "src"),
                i.setAttribute(t, e.nodeValue));
            }),
              e.text && (i.text = e.text),
              i.hasAttribute("src")
                ? (i.addEventListener("load", t),
                  i.addEventListener("error", t))
                : ((i.text = e.text), t());
            try {
              e.parentNode.replaceChild(i, e);
            } catch (e) {
              t();
            }
          }
        : async (t) => {
            function i() {
              e.setAttribute("data-myds-status", "failed"), t();
            }
            try {
              let n = e.getAttribute("data-myds-type"),
                r = e.getAttribute("data-myds-src");
              e.text,
                n
                  ? ((e.type = n), e.removeAttribute("data-myds-type"))
                  : e.removeAttribute("type"),
                e.addEventListener("load", function () {
                  e.setAttribute("data-myds-status", "executed"), t();
                }),
                e.addEventListener("error", i),
                r
                  ? (e.removeAttribute("data-myds-src"), (e.src = r))
                  : (e.src =
                      "data:text/javascript;base64," +
                      window.btoa(unescape(encodeURIComponent(e.text))));
            } catch (e) {
              i();
            }
          })
    );
  }
  async _loadScriptsFromList(e) {
    let t = e.shift();
    return t && t.isConnected
      ? (await this._transformScript(t), this._loadScriptsFromList(e))
      : Promise.resolve();
  }
  _preloadAllScripts() {
    this._batchInjectResourceHints(
      [
        ...this.delayedScripts.normal,
        ...this.delayedScripts.defer,
        ...this.delayedScripts.async,
      ],
      "preload"
    );
  }
  _batchInjectResourceHints(e, t) {
    var i = document.createDocumentFragment();
    e.forEach((e) => {
      let n = (e.getAttribute && e.getAttribute("data-myds-src")) || e.src;
      if (n) {
        let r = document.createElement("link");
        (r.href = n),
          (r.rel = t),
          "preconnect" !== t && (r.as = "script"),
          e.getAttribute &&
            "module" === e.getAttribute("data-myds-type") &&
            (r.crossOrigin = !0),
          e.crossOrigin && (r.crossOrigin = e.crossOrigin),
          e.integrity && (r.integrity = e.integrity),
          i.appendChild(r),
          this.trash.push(r);
      }
    }),
      document.head.appendChild(i);
  }
  _delayEventListeners(e) {
    function t(e, t) {
      !(function (e) {
        function t(t) {
          return n[e].eventsToRewrite.indexOf(t) >= 0 ? "myds-" + t : t;
        }
        !n[e] &&
          ((n[e] = {
            originalFunctions: {
              add: e.addEventListener,
              remove: e.removeEventListener,
            },
            eventsToRewrite: [],
          }),
          (e.addEventListener = function () {
            (arguments[0] = t(arguments[0])),
              n[e].originalFunctions.add.apply(e, arguments);
          }),
          (e.removeEventListener = function () {
            (arguments[0] = t(arguments[0])),
              n[e].originalFunctions.remove.apply(e, arguments);
          }));
      })(e),
        n[e].eventsToRewrite.push(t);
    }
    function i(e, t) {
      let i = e[t];
      Object.defineProperty(e, t, {
        get: () => i || function () {},
        set(n) {
          e["myds" + t] = i = n;
        },
      });
    }
    let n = {};
    t(document, "DOMContentLoaded"),
      t(window, "DOMContentLoaded"),
      t(window, "load"),
      t(window, "pageshow"),
      t(document, "readystatechange"),
      i(document, "onreadystatechange"),
      i(window, "onload"),
      i(window, "onpageshow");
  }
  _delayJQueryReady(e) {
    function t(t) {
      if (t && t.fn && !e.allJQueries.includes(t)) {
        t.fn.ready = t.fn.init.prototype.ready = function (i) {
          return (
            e.domReadyFired
              ? i.bind(document)(t)
              : document.addEventListener("myds-DOMContentLoaded", () =>
                  i.bind(document)(t)
                ),
            t([])
          );
        };
        let i = t.fn.on;
        (t.fn.on = t.fn.init.prototype.on =
          function () {
            if (this[0] === window) {
              function e(e) {
                return e
                  .split(" ")
                  .map((e) =>
                    "load" === e || 0 === e.indexOf("load.")
                      ? "myds-jquery-load"
                      : e
                  )
                  .join(" ");
              }
              "string" == typeof arguments[0] || arguments[0] instanceof String
                ? (arguments[0] = e(arguments[0]))
                : "object" == typeof arguments[0] &&
                  Object.keys(arguments[0]).forEach((t) => {
                    let i = arguments[0][t];
                    delete arguments[0][t], (arguments[0][e(t)] = i);
                  });
            }
            return i.apply(this, arguments), this;
          }),
          e.allJQueries.push(t);
      }
      i = t;
    }
    let i;
    t(window.jQuery),
      Object.defineProperty(window, "jQuery", {
        get: () => i,
        set(e) {
          t(e);
        },
      });
  }
  async _triggerDOMContentLoaded() {
    (this.domReadyFired = !0),
      await this._littleBreath(),
      document.dispatchEvent(new Event("myds-DOMContentLoaded")),
      await this._littleBreath(),
      window.dispatchEvent(new Event("myds-DOMContentLoaded")),
      await this._littleBreath(),
      document.dispatchEvent(new Event("myds-readystatechange")),
      await this._littleBreath(),
      document.mydsonreadystatechange && document.mydsonreadystatechange();
  }
  async _triggerWindowLoad() {
    await this._littleBreath(),
      window.dispatchEvent(new Event("myds-load")),
      await this._littleBreath(),
      window.mydsonload && window.mydsonload(),
      await this._littleBreath(),
      this.allJQueries.forEach((e) => e(window).trigger("myds-jquery-load")),
      await this._littleBreath();
    let e = new Event("myds-pageshow");
    (e.persisted = this.persisted),
      window.dispatchEvent(e),
      await this._littleBreath(),
      window.mydsonpageshow &&
        window.mydsonpageshow({ persisted: this.persisted });
  }
  _handleDocumentWrite() {
    let e = new Map();
    document.write = document.writeln = function (t) {
      let i = document.currentScript;
      i || console.error("WPMyds unable to document.write this: " + t);
      let n = document.createRange(),
        r = i.parentElement,
        s = e.get(i);
      void 0 === s && ((s = i.nextSibling), e.set(i, s));
      let a = document.createDocumentFragment();
      n.setStart(a, 0),
        a.appendChild(n.createContextualFragment(t)),
        r.insertBefore(a, s);
    };
  }
  async _littleBreath() {
    Date.now() - this.lastBreath > 45 &&
      (await this._requestAnimFrame(), (this.lastBreath = Date.now()));
  }
  async _requestAnimFrame() {
    return document.hidden
      ? new Promise((e) => setTimeout(e))
      : new Promise((e) => requestAnimationFrame(e));
  }
  _emptyTrash() {
    this.trash.forEach((e) => e.remove());
  }
  static run() {
    let e = new MydsLazyLoadScripts();
    e._addUserInteractionListener(e);
  }
}
MydsLazyLoadScripts.run();
