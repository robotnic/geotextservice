<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
<xsl:strip-space  elements="*"/>
<xsl:template match="/">

{
<xsl:apply-templates select="/*|text()"/>
}
</xsl:template>

<xsl:template match="*">
	<div style="margin-left:50px;width:900;border:0px solid black">
	<xsl:text>"</xsl:text>
	<xsl:value-of select="name()"/>
	<xsl:text>":{ </xsl:text>
	<xsl:if test="count(@*)&gt;0">
	<xsl:text> </xsl:text>
	<xsl:for-each select="@*">
		<div style="margin-left:50px;border:0px solid black">
		<xsl:text>"@</xsl:text>
		<xsl:value-of select="name()"/>":"<xsl:value-of select="."/>
		<xsl:text>"</xsl:text>
		<xsl:if test="position()!=last()">
			<xsl:text>,</xsl:text>
		</xsl:if>
		</div>
	</xsl:for-each>
	<xsl:text>,</xsl:text>
	</xsl:if>
        <xsl:apply-templates select="*|text()"/>
		<xsl:text>}</xsl:text>
		<xsl:if test="position()!=last()">
			<xsl:text>, </xsl:text> 
		</xsl:if>
	</div>
</xsl:template>

<xsl:template match="text()">
	<div style="margin-left:50px;border:0px solid black">
	<xsl:text>"#text:":"</xsl:text>
	<xsl:value-of select="."/>
	<xsl:text>"</xsl:text>
		<xsl:if test="position()!=last()">
			<xsl:text>, </xsl:text>
		</xsl:if>
	</div>
</xsl:template>



</xsl:stylesheet>
