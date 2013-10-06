<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="$ {locale_code[:2]}" lang="$ {locale_code[:2]}">
<head>
    <title><%block name="title">
        % if page_title is not None:
            ${page_title} » ${site_title}
        % else:
            ${site_title} » ${site_claim}
        % endif
    </%block></title>
    <meta http-equiv="Content-Type" content="text/html;charset=UTF-8"/>

    ## <meta name="keywords" content="${_(u'META_SITE_Keywords')}" />
    ## <meta name="description" content="${_(u'META_SITE_Description')}" />

    <meta name="application-name" content="elmyra.ip.access.epo" />
    ## +Snippets
    <meta itemprop="name" content="elmyra.ip.access.epo">
    <%block name="plus_description"></%block>

    <link rel="shortcut icon" href="${url.app}/favicon.ico" />

    <!-- Le HTML5 shim, for IE6-8 support of HTML5 elements -->
    <!--[if lt IE 9]>
        <script src="${url.app}/js/html5.js"></script>
    <![endif]-->

    ## <link rel="apple-touch-icon-precomposed"
    ##       sizes="144x144" href="${url.app}/ico/apple-touch-icon-144-precomposed.png" />
    ## <link rel="apple-touch-icon-precomposed"
    ##       sizes="114x114" href="${url.app}/ico/apple-touch-icon-114-precomposed.png" />
    ## <link rel="apple-touch-icon-precomposed"
    ##       sizes="72x72" href="${url.app}/ico/apple-touch-icon-72-precomposed.png" />
    ## <link rel="apple-touch-icon-precomposed"
    ##       href="${url.app}/ico/apple-touch-icon-57-precomposed.png" />
</head>

<body>
${self.body()}
</body>
</html>
