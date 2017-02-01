// adapted from http://stackoverflow.com/questions/2631820/im-storing-click-coordinates-in-my-db-and-then-reloading-them-later-and-showing/2631931#2631931
var getXPathTo = function (element){
    /* -- if we allow id() in XPath
    if (element.id !== '')
        return 'id("' + element.id + '")';
    */
    // Recursion breaker: at document root
    if (element === document)
        return '';
    // Recursively find path of this element by counting siblings
    var count = 0;
    var hit = 0;
    var siblings = element.parentNode.childNodes;
    for (var i=0; i<siblings.length; i++) {
        if (siblings[i].nodeType===1 && siblings[i].tagName===element.tagName)
            count++;
        if (siblings[i] === element)
            hit = count;
        if (count > 1 && hit >= 1)
            break;
    };
    // Return XPath
    if (hit == 1 && count == 1) {
        return getXPathTo(element.parentNode)+'/'+element.tagName.toLowerCase();
    } else {
        return getXPathTo(element.parentNode)+'/'+element.tagName.toLowerCase()+'['+hit+']';
    };
};
return getXPathTo(arguments[0]);
