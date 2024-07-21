from django import template
import json

register = template.Library()

@register.filter
def render_tree(tree):
    return render_tree_html(tree)

def render_tree_html(tree):
    if isinstance(tree, dict):
        html = '<ul>'
        for key, subtree in tree.items():
            html += f'<li>{key}'
            if isinstance(subtree, dict):
                html += render_tree_html(subtree)
            html += '</li>'
        html += '</ul>'
        return html
    return ''
