[Facilitating the discovery of public datasets](https://research.googleblog.com/2017/01/facilitating-discovery-of-public.html)
------------------------------------------------------------------------------------------------------------------------------

Tuesday, January 24, 2017
Posted by Natasha Noy, Google Research and Dan Brickley, Open Source
Programs Office  
  
  
There are many hundreds of data repositories on the Web, providing
access to tens of thousands—or millions—of datasets. National and
regional governments, scientific publishers and consortia, commercial
data providers, and others [publish
data](https://en.wikipedia.org/wiki/Open_data#Major_sources) for fields
ranging from [social science](http://icpsr.umich.edu/) to [life
science](http://www.omicsdi.org/) to [high-energy
physics](http://hepdata.net/) to [climate science](http://rda.ucar.edu/)
and more. Access to this data is critical to facilitating
reproducibility of research results, enabling scientists to build on
others’ work, and providing data journalists easier access to
information and its provenance. For these reasons, many publishers and
funding agencies now require that scientists make their research data
available publicly.  
  
However, due to the volume of data repositories available on the Web, it
can be extremely difficult to determine not only where is the dataset
that has the information that you are looking for, but also the veracity
or provenance of that information. Yet, there is no reason why searching
for datasets shouldn’t be as easy as searching for recipes, or jobs, or
movies. These types of searches are often open-ended ones, where some
structure over the search space makes the exploration and serendipitous
discovery possible.  
  
To provide better discovery and rich content for books, movies, events,
recipes, reviews and a number of other content categories with Google
Search, we [rely](https://developers.google.com/search/docs/guides/) on
structured data that content providers embed in their sites using
[schema.org](http://schema.org/) vocabulary. To facilitate similar
capabilities for datasets, we have [recently published new
guidelines](https://developers.google.com/search/docs/data-types/datasets)
to help data providers describe their datasets in a structured way,
enabling Google and others to link this structured metadata with
information describing locations, scientific publications, or even
[Knowledge
Graph](https://www.google.com/intl/bn/insidesearch/features/search/knowledge.html),
facilitating data discovery for others. We hope that this metadata will
help us improve the discovery and reuse of public datasets on the Web
for everybody.  
  
The schema.org approach for describing datasets is based on an effort
recently standardized at W3C (the [Data Catalog
Vocabulary](https://www.w3.org/TR/vocab-dcat/)), which we expect will be
a foundation for future elaborations and improvements to dataset
description. While these industry
[discussions](https://www.w3.org/2016/11/sdsvoc/) are evolving, we are
confident that the standards that already exist today provide a solid
basis for building a data ecosystem.  
  
**Technical Challenges**  
While we have released the guidelines on publishing the metadata, many
technical challenges remain before search for data becomes as seamless
as we feel it should be. These challenges include:  
-   **Defining more consistently what constitutes a dataset:** For
    example, is a single table a dataset? What about a collection of
    related tables? What about a protein sequence? A set of images? An
    API that provides access to data? We hope that a better
    understanding of what a dataset is will emerge as we gain more
    experience with how data providers define, describe, and use data.
-   **Identifying datasets:** Ideally, datasets should have permanent
    identifiers conforming to some well known scheme that enables us to
    identify them uniquely, but often they don’t. Is a URL for the
    metadata page a good identifier? Can there be multiple identifiers?
    Is there a primary one?
-   **Relating datasets to each other**: When are two records describing
    a dataset “the same” (for instance, if one repository copies
    metadata from another )? What if an aggregator provides more
    metadata about the same dataset or cleans the data in some useful
    way? We are working on clarifying and defining these relationships,
    but it is likely that consumers of metadata will have to assume that
    many data providers are using these predicates imprecisely and need
    to be tolerant of that.
-   **Propagating metadata between related datasets:** How much of the
    metadata can we propagate among related datasets? For instance, we
    can probably propagate provenance information from a composite
    dataset to the datasets that it contains. But how much does the
    metadata “degrade” with such propagation? We expect the answer to be
    different depending on the application: metadata for search
    applications may be less precise than, say, for data integration.
-   **Describing content of datasets:** How much of the dataset content
    should we describe to enable support for queries similar to those
    used in [Explore for Docs, Sheets and
    Slides](https://docs.googleblog.com/2016/09/ExploreinDocsSheetsSlides.html),
    or other exploration and reuse of the content of the datasets (where
    license terms allow, of course)? How can we efficiently use content
    descriptions that providers already describe in a declarative way
    using [W3C standards for describing semantics of Web resources and
    linked data](https://www.w3.org/standards/semanticweb/)?

In addition to the technical and social challenges that we’ve just
listed, many remaining research challenges touch on longer term
open-ended research: Many datasets are described in unstructured way, in
captions, figures, and tables of scientific papers and other documents.
We can build on
[other](https://www.eecis.udel.edu/~shatkay/papers/BIBM2011.pdf)
[promising](https://clgiles.ist.psu.edu/pubs/ICDAR2013-search-figures.pdf)
[efforts](https://ai2-website.s3.amazonaws.com/publications/pdf2.0.pdf)
to extract this metadata. While we have a reasonable handle on ranking
in the content of Web search, ranking datasets is often a [challenging
problem](https://research.google.com/pubs/pub45390.html): we don’t know
yet if the same signals that work for ranking Web pages will work
equally well for ranking datasets. In the cases where the dataset
content is public and available, we may be able to extract additional
semantics about the dataset, for example, by learning the types of
values in different fields. Indeed, can we understand the content enough
to enable data integration and discovery of related resources?  
  
**A Call to Action**  
As any ecosystem, a data ecosystem will thrive only if a variety of
players contribute to it:  
-   **For data providers, both individual providers and data
    repositories:** publishing structured metadata using
    [schema.org](http://schema.org/),
    [DCAT](https://www.w3.org/TR/vocab-dcat/),
    [CSVW](https://www.w3.org/2013/csvw/wiki/Main_Page), and other
    community standards will make this metadata available for others to
    discover and use.
-   **For data consumers (from scientists to data journalists and
    more):** citing data properly, much as we cite scientific
    publications (see, for example, a recently proposed
    [approach](http://biorxiv.org/content/biorxiv/early/2016/12/28/097196.full.pdf)).
-   **For developers:** to contribute to
    [expanding](https://github.com/schemaorg/schemaorg) schema.org
    metadata for datasets, providing domain-specific vocabularies, as
    well as working on tools and applications that consume this
    rich metadata.

Our ultimate goal is to help foster an ecosystem for publishing,
consuming and discovering datasets. As such, this ecosystem would
include data publishers, aggregators (in the form of large data
repositories that provide additional value by cleaning and reconciling
metadata), search engines that enable data discovery of the data, and,
most important, data consumers.

Labels: [Data
Discovery](https://research.googleblog.com/search/label/Data%20Discovery)
, [datasets](https://research.googleblog.com/search/label/datasets) ,
[schema.org](https://research.googleblog.com/search/label/schema.org)



