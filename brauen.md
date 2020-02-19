---
layout: default
title: Brauen
math: false
---

<div class="home">
{%- if page.title -%}
<h1 class="page-heading">{{ page.title }}</h1>
{%- endif -%}

<div class="container-fluid mb-3">
<p>
Auf dieser Seite sammle ich meine Brau-Experimente. Die Posts dienen vor allem als Tagebuch und Referenz fuer spaeter, koennen aber prinzipiell auch als (sehr knapp gehaltene) Anleitung verwendet werden.
</p>
</div>

{%- if site.posts.size > 0 -%}
<!-- <div class="col-sm-12" id="main-content"> -->
<div class="row">
{%- for post in site.posts -%}
{%- if post.categories contains 'brauen' -%}
<div class ="col-4">
<div class="card bg-light mb-3" >
{%- if post.related_image -%}
<a href="{{ post.url }}"><img class="img-responsive" src="{{ post.related_image }}" style="width: 100%;"></a>
{%- else -%}
<a href="{{ post.url }}"><img class="img-responsive" src="thumbnails/grey.jpg" style="width: 100%;"></a>
{%- endif -%}
{{ post.date | date: "%Y-%m-%d" }}<br>
<h3 class="card-title"><a href ="{{ post.url}}" style="color: inherit;">{{ post.title }}</a></h3>
</div>
</div>
{%- endif -%}
{%- endfor -%}
{%- endif -%}

</div>
</div>
