/*
 * Copyright (c) Meta Platforms, Inc. and affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */

use crate::django_testcase;

django_testcase!(
    test_annotate_adds_keyword_attributes_to_rows,
    r#"
from typing import Any, assert_type

from django.db import models
from django.db.models.query import QuerySet

class Article(models.Model):
    title = models.CharField(max_length=100)

annotated = Article.objects.annotate(extra_title=models.F("title"))
assert_type(annotated, QuerySet[Article, Article])
assert_type(annotated.create(title="plain"), Article)

article = annotated[0]
assert_type(article, Article)
assert_type(article.title, str)
assert_type(article.extra_title, Any)
Article().extra_title  # E: Object of class `Article` has no attribute `extra_title`

filtered = annotated.filter(title="kept")[0]
assert_type(filtered, Article)
assert_type(filtered.extra_title, Any)

for chained in annotated.annotate(second_title=models.F("title")):
    assert_type(chained, Article)
    assert_type(chained.extra_title, Any)
    assert_type(chained.second_title, Any)

for values_row in Article.objects.values("title").annotate(extra_title=models.F("title")):
    values_row.extra_title  # E: Object of class `dict` has no attribute `extra_title`
"#,
);

// https://github.com/pyrefly-org/pyrefly/issues/5677
django_testcase!(
    test_annotate_attributes_survive_generic_calls,
    r#"
from typing import Any, assert_type

from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)

annotated = Article.objects.annotate(extra=models.F("title"))

for a in annotated:
    assert_type(a.extra, Any)
for b in annotated.only("title"):
    assert_type(b.extra, Any)
for c in annotated.iterator():
    assert_type(c.extra, Any)
assert_type(next(annotated.iterator()).extra, Any)
for d in [annotated.get()]:
    assert_type(d.extra, Any)
first = annotated.first()
if first is not None:
    assert_type(first.extra, Any)

def returned():
    return Article.objects.annotate(extra=models.F("title"))

for e in returned():
    assert_type(e.extra, Any)
"#,
);

django_testcase!(
    test_many_chained_annotate_calls,
    r#"
from typing import Any, assert_type

from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)

qs = Article.objects.annotate(a0=models.F("title"))
qs = qs.annotate(a1=models.F("title")).filter(title="x")
qs = qs.annotate(a2=models.F("title")).only("title")
qs = qs.annotate(a3=models.F("title")).exclude(title="y")
qs = qs.annotate(a4=models.F("title")).order_by("title")
qs = qs.annotate(a5=models.F("title")).distinct()
qs = qs.annotate(a6=models.F("title")).all()
qs = qs.annotate(a7=models.F("title"))

row = qs.get()
assert_type(row, Article)
assert_type(row.title, str)
assert_type(row.a0, Any)
assert_type(row.a7, Any)
row.missing  # E: Object of class `Article` has no attribute `missing`
"#,
);

django_testcase!(
    test_annotate_shadows_method,
    r#"
from typing import Any, assert_type

from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)

    def total(self) -> int:
        return 0

    @property
    def headline(self) -> str:
        return self.title

row = Article.objects.annotate(total=models.Count("id"), headline=models.F("title")).get()
assert_type(row.total, Any)
assert_type(row.headline, str)
"#,
);
