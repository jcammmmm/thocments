# About
The script `tex2chtml-page` was taken from the [MathJax](https://github.com/mathjax/MathJax-demos-node) demos node repositoy; a well curated and detailed repo devoted to examples on how to use MathJax in a node environment. In particular, this script was taken from the `jsdom` examples.   
The current app makes use of [jsdom](https://github.com/jsdom/jsdom) because the default one [liteDOM](https://github.com/litejs/dom) cannot handle complex html files such as those that appear on this blogs.

# Usage
This subsection deals on how to render your _neat post_ on the server. The main advantage of this is that your _neat posts_ will render more quickly because your _Latex_ equations will be rendered into HTML on the server. One disadvantage is that changes on your _neat posts_ will require an additional step in order to be published, but, given the change rate of your post this cannot be count as a disadvantage.

  

# Troubleshooting
If any of the required packages are not found, you need to set the `NODE_PATH` environment variable to the path returned by the `npm root -g` command.

## Useful commands

    C:\Users\Camilo\AppData\Roaming\npm\node_modules

    C:\Users\Camilo\Data\repo.m\semiinfinite-prog-chebyshev

    node ..\neatposts\src\text2chtml\tex2chtml-page 

    npm config get prefix

    npm list -g

    npm root -g