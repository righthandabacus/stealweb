(function(){
    /* Scan the whole DOM for all elements, for each, collect the geometry, visibility,
     * color, text, HTML and others, then return a huge array of such attributes
     */
    function addpath(nodepath, element, xpath) {
        var rect = element.getBoundingClientRect();
        var style = window.getComputedStyle(element, null);
        var offsetx = window.pageXOffset;
        var offsety = window.pageYOffset;
        var display = (style.display != 'none')?1:0;
        var visible = (style.visibility == 'visible')?1:0;
        var fgcolor = style.color;
        var bgcolor = style.getPropertyValue('background-color');
        var fontsize = style.getPropertyValue('font-size');
        var text = element.innerText;
        var html = element.outerHTML;
        nodepath.push([xpath, display, visible, rect.left+offsetx, rect.top+offsety, rect.width, rect.height, fgcolor, bgcolor, fontsize, text, html]);
    };
    function pathwalker(nodepath, element, basepath) {
        var children = element.childNodes;
        var tagmap = {} // offset list for each children's tag, help building XPath
        for (var i=0; i<children.length; i++) {
            if (!children[i].tagName) continue;
            var tag = children[i].tagName.toLowerCase();
            if (tagmap[tag]) {
                tagmap[tag].push(i);
            } else {
                tagmap[tag] = [i];
            };
        };
        for (var i=0; i<children.length; i++) {
            if (!children[i].tagName) {
                continue // no tag name, likely comment node
            };
            var tag = children[i].tagName.toLowerCase();
            /*
            if (tag.indexOf(':') >= 0) {
                continue // ignore everything with a prefix or namespace
            };
            */
            var xpath = basepath+'/'+tag;
            if (tagmap[tag].length > 1) {
                xpath = xpath + '[' + (tagmap[tag].indexOf(i)+1) + ']';
            };
            addpath(nodepath, children[i], xpath);
            pathwalker(nodepath, children[i], xpath);
        };
    };
    var nodepath = [];
    pathwalker(nodepath, document, ''); // collect all attributes
    var windowparam = { // browser geometry parameters
        addr: document.location.href,
        innerWidth: window.innerWidth,
        innerHeight: window.innerHeight,
        outerWidth: window.outerWidth,
        outerHeight: window.outerHeight,
        pageXOffset: window.pageXOffset,
        pageYOffset: window.pageYOffset,
        scrollX: window.scrollX,
        scrollY: window.scrollY,
        screenLeft: window.screenLeft,
        screenTop: window.screenTop,
    };
    if (window.screen) {
        windowparam.availHeight = window.screen.availHeight;
        windowparam.availWidth = window.screen.availWidth;
        windowparam.availLeft = window.screen.availLeft;
        windowparam.availTop = window.screen.availTop;
        windowparam.width = window.screen.width;
        windowparam.height = window.screen.height;
        windowparam.colorDepth = window.screen.colorDepth;
    };
    get_attr_callback(nodepath, windowparam); // return all attributes
})();

