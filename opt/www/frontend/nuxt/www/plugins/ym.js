export default ({ app }) => {

  if (process.env.NODE_ENV !== 'production') return;

 (function(m,e,t,r,i,k,a){m[i]=m[i]||function(){(m[i].a=m[i].a||[]).push(arguments)};
   m[i].l=1*new Date();k=e.createElement(t),a=e.getElementsByTagName(t)[0],k.async=1,k.src=r,a.parentNode.insertBefore(k,a)})
   (window, document, "script", "https://mc.yandex.ru/metrika/tag.js", "ym");

   ym(56657455, "init", {
        clickmap:true,
        trackLinks:true,
        accurateTrackBounce:true,
        webvisor:true,
        ecommerce:"dataLayer"
   });
   ym(56657455, 'hit', '/', {
    title: 'Web разработчик Django',
    
});

  app.router.afterEach((to, from) => {
    ym(56657455, 'init', to.fullPath);
  });

    app.router.afterEach((to, from) => {
    ym(56657455, 'hit', to.fullPath);
  });
}
