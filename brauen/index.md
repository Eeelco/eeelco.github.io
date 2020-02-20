---
layout: default
title: Brauen
mycat: Brauen
math: false
pagination:
    enabled: true
    category: brauen
---

<div class="home">
{%- if page.mycat -%}
<h1 class="page-heading">{{ page.mycat }}</h1>
{%- endif -%}

<div class="container-fluid mb-3">
<p>
Auf dieser Seite sammle ich meine Brau-Experimente. Die Posts dienen vor allem als Tagebuch und Referenz fuer spaeter, koennen aber prinzipiell auch als (sehr knapp gehaltene) Anleitung verwendet werden.
</p>
</div>

<div class="row">
{%- for post in paginator.posts -%}
<div class ="col-4">
<div class="card bg-light mb-3" >
{%- if post.related_image -%}
<a href="{{ post.url }}"><img class="img-responsive" src="{{ post.related_image }}" style="width: 100%;"></a>
{%- else -%}
<a href="{{ post.url }}"><img class="img-responsive" src="/thumbnails/grey.jpg" style="width: 100%;"></a>
{%- endif -%}
{{ post.date | date: "%Y-%m-%d" }}<br>
<h3 class="card-title"><a href ="{{ post.url}}" style="color: inherit;">{{ post.title }}</a></h3>
</div>
</div>
{%- endfor -%}
</div>

 {% if paginator.total_pages > 1 %}
  <ul class="pager">
      {% if paginator.first_page %}
      <li class="previous">
          <a href="{{ paginator.first_page_path | prepend: site.baseurl | replace: '//', '/' }}">First</a>
      </li>
      {% endif %}

      {% if paginator.previous_page %}
      <li class="previous">
          <a href="{{ paginator.previous_page_path | prepend: site.baseurl | replace: '//', '/' }}">&larr; Newer Posts</a>
      </li>
      {% endif %}

      {% if paginator.page_trail %}
        {% for trail in paginator.page_trail %}
          <li {% if page.url == trail.path %}class="selected"{% endif %}>
              <a href="{{ trail.path | prepend: site.baseurl | replace: '//', '/' | replace '', 'index.html' }}" title="{{trail.title}}">{{ trail.num }}</a>
          </li>
        {% endfor %}
      {% endif %}

      {% if paginator.next_page %}
      <li class="next">
          <a href="{{ paginator.next_page_path | prepend: site.baseurl | replace: '//', '/' }}">Older Posts &rarr;</a>
      </li>
      {% endif %}

       {% if paginator.last_page %}
      <li class="previous">
          <a href="{{ paginator.last_page_path | prepend: site.baseurl | replace: '//', '/' }}">Last</a>
      </li>
      {% endif %}
  </ul>
  {% endif %}
</div>
