<!-- https://www.mathjax.org/MathJax-v3.2.0-available/ -->
<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script> 
<script type="text/javascript" id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3.2.0/es5/tex-chtml.js"></script>

<script>
  /***********************************************************************
   * MATHJAX CONFIGURATION                                               *
   ***********************************************************************/
  function overflowWrap(elem) {
    let wrapper = document.createElement('div');
    wrapper.setAttribute('style', 'overflow-x: scroll;');
    wrapper.appendChild(elem.cloneNode(true));
    elem.parentElement.replaceChild(wrapper, elem);
  }

  // http://docs.mathjax.org/en/latest/options/input/tex.html
  window.MathJax = {
    loader: {
      // http://docs.mathjax.org/en/latest/input/tex/extensions/tagformat.html
      load: [
        '[tex]/tagformat'
      ]
    },
    tex: {
      inlineMath: [['$', '$']],
      // https://docs.mathjax.org/en/v3.2-latest/input/tex/eqnumbers.html
      tags: 'ams',
      packages: {'[+]': ['tagformat']},
      tagformat: {
        number: (n) => n.toString(),
        tag:    (tag) => '(' + tag + ')',
        id:     (id) => '' + id.replace(/\s/g, '_'),
        url:    (id, base) => base + '#' + encodeURIComponent(id),
      }
    },
   startup: {
    /***********************************************************************
     * OVERFLOW FIX                                                        *
     ***********************************************************************/
    pageReady: () => {
      return MathJax.startup.defaultPageReady().then(() => {
        let mjxcon = document.getElementsByTagName('mjx-container');
        // wrap mathjax equations with overflow-x div
        for (mjx of mjxcon)
          if (mjx.hasAttribute('display'))
            overflowWrap(mjx);
        // wrap tables with overflow-x div
        let tables = document.getElementsByTagName('table');
        for (table of tables)
          overflowWrap(table);
      });
      }
    }
  }
</script>