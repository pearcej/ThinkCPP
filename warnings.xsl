<xsl:stylesheet version="1.0"
                xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:output method="xml"/>
  <xsl:template match="@*|node()">
  </xsl:template>
  <xsl:template match="exercise">
    <xsl:message><xsl:value-of select="."/></xsl:message>
  </xsl:template>
</xsl:stylesheet>